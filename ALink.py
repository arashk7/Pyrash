import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF

from arash_test_3.ALinkShape import ALinkShape
from arash_test_3.AUtil import *


class ALink(ALinkShape):
    def __init__(self, param1, param2):
        super().__init__(param1,param2)

        self.param1 = param1
        self.param2 = param2
        self.isDrag = False

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
            self.x = self.x + (pos.x() - self.dragInitPos.x()) / self.parent.scale
            self.y = self.y + (pos.y() - self.dragInitPos.y()) / self.parent.scale
            self.dragInitPos = pos

    def isInside(self, pos):
        begin = QPoint(self.x + self.parent.x, self.y + self.parent.y) * self.parent.scale
        end = QPoint(self.x + self.width + self.parent.x, self.y + self.height + self.parent.y) * self.parent.scale
        if pos.x() > begin.x() and pos.x() < end.x() and pos.y() > begin.y() and pos.y() < end.y():
            return True
        return False
