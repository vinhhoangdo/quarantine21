from PyQt5.QtWidgets import QApplication, QDialog
import sys
from math import *
from PyQt5.uic import loadUi


class Current(QDialog):
    def __init__(self):
        super(Current, self).__init__()
        loadUi("C:\\Users\\Vinh\\Desktop\\GUIpy\\equation.ui",self)
        self.setWindowTitle("QEC")

        self.solve.clicked.connect(self.Solve_func)
        self.clear.clicked.connect(self.Clear_func)
        self.exit.clicked.connect(self.Exit_func)
        self.result.setText("Please insert three coefficients...")

    def Solve_func(self):
        a = float(self.coe_1.text())
        b = float(self.coe_2.text())
        c = float(self.coe_3.text())
        # Ax^2 + Bx + C = 0
        if a == 0:
            self.result.setText("<font color=\"red\">Coefficient a can not be 0</font>")
            if b == 0:
                if c == 0:
                    self.result.setText("<font color=\"blue\">Infinite!</font>")
                else:
                    self.result.setText("<font color=\"red\">Impossible Equation!</font>")
        else:
            d = b ** 2 - 4 * a * c
            if d > 0:
                x1 = (-b + sqrt(d))/(2*a)
                x2 = (-b - sqrt(d))/(2*a)
                self.result.setText("x1 = {x1:.4f}\nx2 = {x2:.4f}".format(x1=x1, x2=x2))
            elif d == 0:
                self.result.setText("x1 = x2 = {x:.4f}".format(x=-b/(2*a)))
            else:
                self.result.setText("<font color=\"red\">Impossible Equation!</font>")

    def Clear_func(self):
        self.coe_1.clear()
        self.coe_2.clear()
        self.coe_3.clear()
        self.result.setText("Please insert three coefficients...")

    def Exit_func(self):
        window.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Current()
    window.show()
    sys.exit(app.exec_())
