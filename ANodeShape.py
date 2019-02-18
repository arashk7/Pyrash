import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPainter, QBrush, QColor, QFont
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF


class ANodeShape:
    def __init__(self, name='None', x=100, y=100, width=100, height=100):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = QColor(150, 150, 150, 200)
        self.hoverColor = QColor(150, 150, 150, 255)
        self.selectColor = QColor(250, 250, 250, 200)
        self.drawColor = self.color

        self.selected = False
        self.name = name
        self.parent=None
        self.scale = 1
        self.incomingParams = list()
        self.outgoingParams = list()

    def draw(self, qp):
        # print('draw')
        self.scale=self.parent.scale

        # Draw rect
        begin = QPoint(self.parent.x*self.parent.scale+self.x * self.parent.scale, self.parent.y*self.parent.scale+self.y * self.parent.scale)
        end = QPoint(self.parent.x*self.parent.scale+self.x * self.parent.scale + self.width * self.parent.scale, self.parent.y*self.parent.scale+self.y * self.parent.scale + self.height * self.parent.scale)
        solid = QBrush(self.drawColor)
        qp.setBrush(solid)
        qp.drawRoundedRect(QRect(begin, end), 20 * self.parent.scale, 20 * self.parent.scale)

        # Draw Title
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QFont("arial", 10*self.parent.scale))
        qp.translate(begin)
        qp.drawText(QtCore.QRectF(0, 0, self.width * self.parent.scale, 25 * self.parent.scale),
                    QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop, self.name)
        qp.translate(begin * -1)

        for p in self.incomingParams:
            p.draw(qp)

        for p in self.outgoingParams:
            p.draw(qp)