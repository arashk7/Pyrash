import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF

from arash_test_3.ANodeShape import ANodeShape
from arash_test_3.AParam import AParam
from arash_test_3.AUtil import *


class ANode(ANodeShape):
    def __init__(self, parent, name='None', x=100, y=100, width=100, height=100):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.isDrag = False
        self.dragInitPos = QPoint(0, 0)
        self.parent=parent


        self.incomingParams.append(AParam(self,0,"in_0",AParamType.Input))
        # self.incomingParams.append(AParam(self, 1, "in_1", AParamType.Input))
        # self.incomingParams.append(AParam(self, 2, "in_2", AParamType.Input))

        self.outgoingParams.append(AParam(self,0,'out_0',AParamType.Output))

        max_param=max(len(self.incomingParams),len(self.outgoingParams))
        print(max_param)
        self.height+=30*max_param

    def onMouseButtonDown(self, pos, btn):
        self.isDrag = True
        self.dragInitPos = pos
        print('press')

    def onMouseButtonUp(self, pos, btn):
        self.isDrag = False
        print('release')

    def onMouseMove(self, pos):
        # print('move')
        if self.isDrag:
            self.x = self.x + (pos.x()-self.dragInitPos.x())/self.parent.scale
            self.y = self.y + (pos.y()-self.dragInitPos.y())/self.parent.scale
            self.dragInitPos=pos

    def isInside(self, pos):
        begin = QPoint(self.x+self.parent.x, self.y+self.parent.y)*self.parent.scale
        end = QPoint(self.x + self.width+self.parent.x, self.y + self.height+self.parent.y)*self.parent.scale
        if pos.x() > begin.x() and pos.x() < end.x() and pos.y()>begin.y() and pos.y()<end.y():
            return True
        return False
