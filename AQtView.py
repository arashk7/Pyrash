import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF, QEvent
from arash_test_3.AView import AView
from arash_test_3.AUtil import *

class AQtView(QtWidgets.QWidget):
    def __init__(self, x=100, y=100, width=1024, height=768):
        super().__init__()
        self.setGeometry(x, y, width, height)
        self.drawScale = 1
        self.pan=QPoint(0,0)
        self.x_view=x
        self.y_view=y;
        self.width_view=width
        self.height_view=height
        self.color_view=QColor(57,57,57,255)

        self.view=AView(-700,-200,1920*1.3,1138*1.3)
        self.view.parent=self

        self.show()
        self.setMouseTracking(True)

    def paintEvent(self, event):
        qp = QPainter(self)
        self.view.draw(qp)

    def mousePressEvent(self, event):
        btn = AMouseButton.NoButton
        if event.buttons() == QtCore.Qt.NoButton:
            btn = AMouseButton.NoButton
        elif event.buttons() == QtCore.Qt.LeftButton:
            btn = AMouseButton.LeftButton
        elif event.buttons() == QtCore.Qt.RightButton:
            btn = AMouseButton.RightButton
        elif event.buttons() == QtCore.Qt.MidButton:
            btn = AMouseButton.MidButton

        self.view.onMouseButtonDown(event.pos(),btn)
        print('press')
        self.update()

    def mouseReleaseEvent(self, event):
        btn = AMouseButton.NoButton
        if event.buttons() == QtCore.Qt.NoButton:
            btn = AMouseButton.NoButton
            btn = AMouseButton.MidButton
        elif event.buttons() == QtCore.Qt.LeftButton:
            btn = AMouseButton.LeftButton
        elif event.buttons() == QtCore.Qt.RightButton:
            btn = AMouseButton.RightButton
        elif event.buttons() == QtCore.Qt.MidButton:
            btn = AMouseButton.MidButton

        self.view.onMouseButtonUp(event.pos(),btn)
        print('release')
        self.update()

    def mouseMoveEvent(self, event):
        # print('move')
        self.view.onMouseMove(event.pos())
        self.update()

    def wheelEvent(self, event):
        step = event.angleDelta().y() / 3500
        self.view.onMouseWheel(event.pos(),step)

        self.update()

