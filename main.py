import sys

from UI import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Program(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_circle)
        self.x1 = 50
        self.y1 = 50
        self.x2 = 0
        self.y2 = 0
        self.color = (0, 0, 0)
        self.flag = False

    def create_circle(self):
        self.flag = True
        self.x2 = self.x1 + randint(5, 300)
        self.y2 = self.x2
        self.color = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(*self.color))
            qp.drawEllipse(self.x1, self.y1, self.x2, self.y2)
            qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = Program()
    program.show()
    sys.exit(app.exec_())