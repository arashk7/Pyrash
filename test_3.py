import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from arash_test_3.AQtView import AQtView


app = QtWidgets.QApplication(sys.argv)
panel = AQtView()
panel.show()
app.aboutToQuit.connect(app.deleteLater)
sys.exit(app.exec_())