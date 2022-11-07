import sys

from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        w = randint(50, 150)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(QPoint(200, 250), w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = MyWidget()
    db.show()
    sys.exit(app.exec())