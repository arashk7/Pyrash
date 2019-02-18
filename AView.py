import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF, QEvent
from arash_test_3.AViewShape import AViewShape
from arash_test_3.ANode import ANode
from arash_test_3.ALink import ALink
from arash_test_3.AParam import AParam
from arash_test_3.AUtil import *

class AView(AViewShape):
    def __init__(self, x=100, y=100, width=1024, height=768):
        super().__init__()
        self.x = x
        self.y = y;
        self.width = width
        self.height = height
        self.color = QColor(100, 100, 100, 100)
        self.isDrag=False
        self.initDragPos=QPoint(0,0)
        self.parent=None


        self.nodes['Input_1']=ANode(self, 'Input_1', 500, 600, 200, 40)
        self.nodes['Input_2']=ANode(self, 'Input_2', 600, 900, 200, 40)
        self.nodes['Conv2D_1']=ANode(self, 'Conv2D_1', 700, 600, 200, 40)
        self.nodes['Conv2D_2']=ANode(self, 'Conv2D_2', 800, 900, 200, 40)
        self.nodes['Merge_1']=ANode(self, 'Merge_1', 900, 900, 200, 40)
        # self.nodes['Merge_1'].incomingParams.append(AParam(self,1,"in_1",AParamType.Input))

        self.links.append(ALink(self.nodes['Input_1'].outgoingParams[0],self.nodes['Conv2D_1'].incomingParams[0]))
        self.links.append(ALink(self.nodes['Input_2'].outgoingParams[0], self.nodes['Conv2D_2'].incomingParams[0]))
        self.links.append(ALink(self.nodes['Conv2D_1'].outgoingParams[0], self.nodes['Merge_1'].incomingParams[0]))
        self.links.append(ALink(self.nodes['Conv2D_2'].outgoingParams[0], self.nodes['Merge_1'].incomingParams[0]))


    def onMouseMove(self,pos):
        # print('move')
        begin = QPoint(self.x, self.y)*self.scale
        end = QPoint(self.x + self.width, self.y + self.height)*self.scale
        if self.isDrag:
            dif=pos-self.initDragPos
            if begin.x()+dif.x()<0 and begin.y()+dif.y()<0 and end.x()+dif.x()>self.parent.width_view and end.y()+dif.y()>self.parent.height_view:
                self.x+=dif.x()*(2-self.scale)
                self.y+=dif.y()*(2-self.scale)
            self.initDragPos=pos

        for n in self.nodes:
            self.nodes[n].onMouseMove(pos)

    def onMouseButtonDown(self,pos,btn):
        print('press')
        if btn==AMouseButton.MidButton:
            self.isDrag = True
            self.initDragPos=pos
        for n in self.nodes:
            if self.nodes[n].isInside(pos):
                self.nodes[n].onMouseButtonDown(pos, btn)
                print('1')
    def onMouseButtonUp(self,pos,btn):
        print('release')
        self.isDrag=False
        for n in self.nodes:
            if self.nodes[n].isInside(pos):
                self.nodes[n].onMouseButtonUp(pos, btn)

    def onMouseWheel(self,pos,step):

        if 0 < self.scale + step < 2:
            self.scale+=step
        dif_x=(self.parent.width_view / 2 - pos.x()) / 50
        dif_y = (self.parent.height_view / 2 - pos.y()) / 50
        if step>0:
            if self.x+dif_x<=0:
                self.x += dif_x
            if self.y + dif_y <= 0:
                self.y += dif_y

        else:
            if self.x - dif_x <= 0:
                self.x -= dif_x
            if self.y - dif_y <= 0:
                self.y -= dif_y

    def isInside(self,pos):
        begin=QPoint(self.x,self.y)
        end=QPoint(self.x+self.width,self.y+self.height)
        if pos>begin and pos<end:
            return True
        return False