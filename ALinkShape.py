import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont, QPainterPath,QPen
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF
from arash_test_3.AParam import AParam
from arash_test_3.AUtil import *

class ALinkShape:
    def __init__(self,param1,param2):
        super().__init__()
        self.param1 = param1
        self.param2 = param2
        self.color = QColor(255, 255, 255, 255)
        self.hoverColor = QColor(150, 150, 150, 255)
        self.selectColor = QColor(250, 250, 250, 200)
        self.drawColor = self.color

        self.width=5
        self.selected = False
        self.parent=None
        self.start=QPoint(0,0)
        self.end=QPoint(0,0)


    def draw(self, qp):
        self.start=self.param1.anchorPos
        self.end=self.param2.anchorPos

        qp.setPen(QPen(self.drawColor, self.width,QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))

        solid = QBrush(QColor(0, 0, 0, 0))
        qp.setBrush(solid)
        self.drawBezierCurve(qp)

    def drawBezierCurve(self, qp):
        path = QPainterPath()
        path.moveTo(self.start.x(), self.start.y())
        # path.quadTo(30, 30, 30, 200)
        mx1 = (self.end.x() + self.start.x()) / 2
        my1 = (self.end.y() + self.start.y()) / 2
        mx2 = (self.end.x() + self.start.x()) / 2
        my2 = (self.end.y() + self.start.y()) / 2
        path.cubicTo(self.start.x(), self.start.y(), mx1, self.start.y(), mx1, my1)
        # path.moveTo(100, 100)
        path.cubicTo(mx2, my2, mx2, self.end.y(), self.end.x(), self.end.y())
        qp.drawPath(path)



