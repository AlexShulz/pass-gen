from PyQt4 import QtGui, QtCore
import sys
import string
import random


class Main_Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.center()
        self.setFixedSize(300, 220)
        self.setWindowTitle("Password generator v.1.0")
        self.setWindowIcon(QtGui.QIcon('key.png'))

        self.pwd_label = QtGui.QLabel(u"Пароль")
        self.num_label = QtGui.QLabel(u"Цифры")
        self.abc_label = QtGui.QLabel(u"Строчные буквы")
        self.Abc_label = QtGui.QLabel(u"Прописные буквы")
        self.sim_label = QtGui.QLabel(u"Спецсимволы")
        self.qnt_label = QtGui.QLabel(u"Количество символов")

        self.pwd_line = QtGui.QLineEdit()
        self.pwd_line.setReadOnly(True)
        self.num_check = QtGui.QCheckBox()
        self.num_check.setChecked(True)
        self.abc_check = QtGui.QCheckBox()
        self.Abc_check = QtGui.QCheckBox()
        self.sim_check = QtGui.QCheckBox()
        self.quantity = QtGui.QSpinBox()
        self.quantity.setMinimum(8)
        self.quantity.setMaximum(28)

        self.gen_btn = QtGui.QPushButton(u"Сгенерировать")

        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.num_check, 0, 0)
        self.grid.addWidget(self.num_label, 0, 1, 1, 6)
        self.grid.addWidget(self.abc_check, 1, 0)
        self.grid.addWidget(self.abc_label, 1, 1, 1, 6)
        self.grid.addWidget(self.Abc_check, 2, 0)
        self.grid.addWidget(self.Abc_label, 2, 1, 1, 6)
        self.grid.addWidget(self.sim_check, 3, 0)
        self.grid.addWidget(self.sim_label, 3, 1, 1, 6)
        self.grid.addWidget(self.quantity, 4, 0, 2, 1)
        self.grid.addWidget(self.qnt_label, 4, 1, 2, 1)
        self.grid.addWidget(self.pwd_label, 6, 0, 2, 2)
        self.grid.addWidget(self.pwd_line, 6, 1, 2, 6)
        self.grid.addWidget(self.gen_btn, 8, 0, 2, 6)

        self.setLayout(self.grid)

        self.connect(self.gen_btn, QtCore.SIGNAL("clicked()"), self.gen_password)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def gen_password(self):
        digits = string.digits
        abc_string = string.ascii_lowercase
        uabc_string = string.ascii_uppercase
        spec_chars = "!@#$%^&*(){}[]?,."
        chars = ""
        if True in [self.num_check.isChecked(), self.abc_check.isChecked(), self.Abc_check.isChecked(),
                    self.sim_check.isChecked()]:
            chars = digits * self.num_check.isChecked() + abc_string*self.abc_check.isChecked() +\
                    uabc_string * self.Abc_check.isChecked() + spec_chars*self.sim_check.isChecked()
            password = ''.join(random.choice(chars) for i in range(self.quantity.value()))
            self.pwd_line.setText(password)
        else:
            informer = QtGui.QMessageBox()
            informer.setWindowTitle("Password generator v.1.0")
            informer.setStandardButtons(QtGui.QMessageBox.Ok)
            informer.setDefaultButton(QtGui.QMessageBox.Ok)
            informer.setText("Необходимо выбрать хотябы один набор символов!")
            informer.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MW = Main_Window()
    MW.show()
    sys.exit(app.exec_())
