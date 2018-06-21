from PyQt4 import QtGui, QtCore
import sys
import string
import random


__version__ = "1.1"

class Main_Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initWindow()
        self.initLabels()
        self.initElements()
        self.initLayout()

    def initWindow(self):
        self.center()
        self.setFixedSize(300, 160)
        self.setWindowTitle("Password generator " + __version__)
        self.setWindowIcon(QtGui.QIcon('key.png'))

    def initLabels(self):
        self.pwd_label = QtGui.QLabel(u"Пароль:")
        self.num_label = QtGui.QLabel(u"Цифры")
        self.abc_label = QtGui.QLabel(u"Строчные буквы")
        self.Abc_label = QtGui.QLabel(u"Прописные буквы")
        self.sim_label = QtGui.QLabel(u"Спецсимволы")
        self.qnt_label = QtGui.QLabel(u"Количество символов")

    def initElements(self):
        self.pwd_line = QtGui.QLineEdit()
        self.pwd_line.setReadOnly(True)
        self.num_check = QtGui.QCheckBox()
        self.num_check.setChecked(True)
        self.abc_check = QtGui.QCheckBox()
        self.Abc_check = QtGui.QCheckBox()
        self.sim_check = QtGui.QCheckBox()
        self.quantity = QtGui.QSpinBox()
        self.quantity.setMinimum(8)
        self.quantity.setMaximum(32)

        self.gen_btn = QtGui.QPushButton(u"Сгенерировать")
        self.cpy_btn = QtGui.QPushButton(u"Скопировать")

    def initLayout(self):
        self.main_layout = QtGui.QVBoxLayout()
        self.grid_layout = QtGui.QGridLayout()
        self.h1_layout = QtGui.QHBoxLayout()
        self.h2_layout = QtGui.QHBoxLayout()
        self.form_layout = QtGui.QFormLayout()
        self.grid_layout.addWidget(self.num_check, 0, 0)
        self.grid_layout.addWidget(self.num_label, 0, 1)
        self.grid_layout.addWidget(self.abc_check, 0, 2)
        self.grid_layout.addWidget(self.abc_label, 0, 3)
        self.grid_layout.addWidget(self.Abc_check, 1, 0)
        self.grid_layout.addWidget(self.Abc_label, 1, 1)
        self.grid_layout.addWidget(self.sim_check, 1, 2)
        self.grid_layout.addWidget(self.sim_label, 1, 3)
        self.h1_layout.addWidget(self.quantity)
        self.h1_layout.addWidget(self.qnt_label)
        self.h1_layout.addStretch()
        self.form_layout.addRow(self.pwd_label, self.pwd_line)
        self.h2_layout.addWidget(self.gen_btn)
        self.h2_layout.addWidget(self.cpy_btn)
        self.form_layout.addRow(self.h2_layout)

        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(self.h1_layout)
        self.main_layout.addLayout(self.form_layout)
        self.setLayout(self.main_layout)

        self.connect(self.gen_btn, QtCore.SIGNAL("clicked()"), self._gen_password)
        self.connect(self.cpy_btn, QtCore.SIGNAL("clicked()"), self._copy_to_clipboard)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def _gen_password(self):
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
            self._show_informer("Необходимо выбрать хотябы один набор символов!")


    def _copy_to_clipboard(self):
        clpbrd = QtGui.QApplication.clipboard()
        text = self.pwd_line.text()
        if text is not None and text != '':
            clpbrd.clear()
            clpbrd.setText(text)
            msg = "Пароль скопирован!"
        else:
            msg = "Пароль ещё не сгенерирован или пуст!"
        self._show_informer(msg)

    def _show_informer(self, text):
        informer = QtGui.QMessageBox()
        informer.setFixedSize(100, 100)
        informer.setWindowTitle("Password generator " + __version__)
        informer.setWindowIcon(QtGui.QIcon('key.png'))
        informer.setStandardButtons(QtGui.QMessageBox.Ok)
        informer.setDefaultButton(QtGui.QMessageBox.Ok)
        informer.setText(text)
        informer.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MW = Main_Window()
    MW.show()
    sys.exit(app.exec_())
