import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont, QPixmap
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF, QEvent,QSize

from arash_test_3.AUtil import *


class AViewShape:
    def __init__(self, x=100, y=100, width=1024, height=768):
        super().__init__()
        self.x = x
        self.y = y;
        self.width = width
        self.height = height
        self.color = QColor(57, 57, 57, 255)
        self.scale = 1.0
        # self.offset=QPoint(0,0)
        self.nodes = dict()
        # self.nodes['add'] = 'asdd'
        self.links = list()

    def draw(self, qp):
        begin = QPoint(self.x, self.y) * self.scale
        end = QtCore.QPoint(self.x + self.width - 2, self.y + self.height - 2) * self.scale
        gradient = QtGui.QRadialGradient(QPointF(begin), 3000)
        gradient.setColorAt(0.0, QtCore.Qt.white)
        gradient.setColorAt(0.2, QtCore.Qt.darkGray)
        gradient.setColorAt(0.8, QtCore.Qt.darkGray)
        gradient.setColorAt(0.99, QtCore.Qt.gray)
        solid = QBrush(self.color)
        qp.setBrush(solid)
        qp.drawRect(QRect(begin, end))



        myPixmap = QtGui.QPixmap('grid2.jpg')
        # myScaledPixmap = myPixmap.scaled(QSize(2,2), QtCore.Qt.KeepAspectRatio)
        # qp.drawPixmap(QRect(QPoint(0,0), QPoint(1920,1138)), myPixmap)
        qp.drawPixmap(QRect(begin, end), myPixmap)
        for n in self.nodes:
            self.nodes[n].draw(qp)
        for l in self.links:
            l.draw(qp)
