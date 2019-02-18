import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF

from arash_test_3.AUtil import *

class AParamShape:
    def __init__(self,param_id=0, name='None', param_type=AParamType.Input ):
        super().__init__()

        self.color = QColor(100, 100, 100, 255)
        self.hoverColor = QColor(150, 150, 150, 255)
        self.selectColor = QColor(250, 250, 250, 200)
        self.drawColor = self.color
        self.anchorColor=QColor(20, 250, 250, 200)
        self.anchorPos=QPoint(0,0)
        self.anchorRadius=10

        self.selected = False
        self.name = name
        self.parent=None
        self.paramID=param_id

        self.paramType=param_type

        self.titleBarHeight=25
        self.paramHeight=30

    def draw(self, qp):
        x=self.parent.parent.x*self.parent.scale+self.parent.x*self.parent.scale
        y=self.parent.parent.y*self.parent.scale+self.parent.y*self.parent.scale
        # Draw rect
        if self.paramType == AParamType.Input:
            begin = QPoint(x, y+self.titleBarHeight*self.parent.scale+self.paramHeight*self.parent.scale*self.paramID)
            end = QPoint(x + (self.parent.width/2) * self.parent.scale, y+self.titleBarHeight*self.parent.scale+self.paramHeight*self.parent.scale*self.paramID+self.paramHeight*self.parent.scale)
            solid = QBrush(self.drawColor)
            qp.setBrush(solid)
            qp.drawRect(QRect(begin, end))
        elif self.paramType == AParamType.Output:
            begin = QPoint(x+ (self.parent.width/2) * self.parent.scale,
                           y + self.titleBarHeight * self.parent.scale + self.paramHeight * self.parent.scale * self.paramID)
            end = QPoint(x + self.parent.width * self.parent.scale,
                         y + self.titleBarHeight * self.parent.scale + self.paramHeight * self.parent.scale * self.paramID + self.paramHeight * self.parent.scale)
            solid = QBrush(self.drawColor)
            qp.setBrush(solid)
            qp.drawRect(QRect(begin, end))

        # Draw Title
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QFont("Arial", 10*self.parent.scale))
        if self.paramType == AParamType.Input:
            qp.translate(begin)
            qp.drawText(QtCore.QRectF(8,0,(self.parent.width/2) * self.parent.scale,self.paramHeight*self.parent.scale),
                        QtCore.Qt.AlignLeft , self.name)
            qp.translate(begin * -1)
        elif self.paramType == AParamType.Output:
            qp.translate(begin)
            qp.drawText(
                QtCore.QRectF(0, 0, (self.parent.width / 2) * self.parent.scale-8, self.paramHeight * self.parent.scale),
                QtCore.Qt.AlignRight, self.name)
            qp.translate(begin * -1)

        #Draw Anchor
        if self.paramType==AParamType.Input:
            solid = QBrush(self.anchorColor)
            qp.setBrush(solid)
            self.anchorPos=begin+QPoint(-5,self.paramHeight/2)*self.parent.scale
            qp.drawEllipse(begin+QPoint(-5,self.paramHeight/2)*self.parent.scale,self.anchorRadius*self.parent.scale,self.anchorRadius*self.parent.scale)
        elif self.paramType == AParamType.Output:
            solid = QBrush(self.anchorColor)
            qp.setBrush(solid)
            self.anchorPos = end + QPoint(5, -self.paramHeight / 2)*self.parent.scale
            qp.drawEllipse(end + QPoint(5, -self.paramHeight / 2)*self.parent.scale, self.anchorRadius*self.parent.scale, self.anchorRadius*self.parent.scale)
