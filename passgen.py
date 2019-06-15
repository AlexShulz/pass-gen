"""The Simple Password Generator.
"""
import random
import sys
import string
from PyQt5 import QtWidgets, QtGui


__version__ = "1.2"

class MainWindow(QtWidgets.QWidget):
    """MainWindow class.
    """
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self._initWindow()
        self._initLabels()
        self._initElements()
        self._initLayout()

    def _initWindow(self):
        self._center()
        self.setFixedSize(380, 180)
        self.setWindowTitle("Password generator " + __version__)
        self.setWindowIcon(QtGui.QIcon('key.png'))

    def _initLabels(self):
        self.pwd_label = QtWidgets.QLabel(u"Пароль:")
        self.num_label = QtWidgets.QLabel(u"Цифры")
        self.abc_label = QtWidgets.QLabel(u"Строчные буквы")
        self.Abc_label = QtWidgets.QLabel(u"Прописные буквы")
        self.sim_label = QtWidgets.QLabel(u"Спецсимволы")
        self.qnt_label = QtWidgets.QLabel(u"Количество символов")

    def _initElements(self):
        self.pwd_line = QtWidgets.QLineEdit()
        self.pwd_line.setReadOnly(True)
        self.num_check = QtWidgets.QCheckBox()
        self.num_check.setChecked(True)
        self.abc_check = QtWidgets.QCheckBox()
        self.Abc_check = QtWidgets.QCheckBox()
        self.sim_check = QtWidgets.QCheckBox()
        self.quantity = QtWidgets.QSpinBox()
        self.quantity.setMinimum(8)
        self.quantity.setMaximum(32)

        self.gen_btn = QtWidgets.QPushButton(u"Сгенерировать")
        self.cpy_btn = QtWidgets.QPushButton(u"Скопировать")

    def _initLayout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.grid_layout = QtWidgets.QGridLayout()
        self.h1_layout = QtWidgets.QHBoxLayout()
        self.h2_layout = QtWidgets.QHBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
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

        # connect signals to generate and copy password
        self.gen_btn.clicked.connect(self.get_password)
        self.cpy_btn.clicked.connect(self.copy_to_clipboard)

    def _center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def _gen_password(self, chars, size):
            password = ''.join(random.choice(chars) for i in range(size))
            return password

    def get_password(self):
        digits = string.digits
        abc_string = string.ascii_lowercase
        uabc_string = string.ascii_uppercase
        spec_chars = "!@#$%^&*(){}[]?,."
        chars = ""
        if True in [self.num_check.isChecked(), self.abc_check.isChecked(), self.Abc_check.isChecked(),
                    self.sim_check.isChecked()]:
            chars = digits * self.num_check.isChecked() + abc_string*self.abc_check.isChecked() +\
                    uabc_string * self.Abc_check.isChecked() + spec_chars*self.sim_check.isChecked()
            password = self._gen_password(chars, self.quantity.value())
            self.pwd_line.setText(password)
        else:
            self.show_informer("Необходимо выбрать хотябы один набор символов!")

    def copy_to_clipboard(self):
        clpbrd = QtWidgets.QApplication.clipboard()
        text = self.pwd_line.text()
        if text is not None and text != '':
            clpbrd.clear()
            clpbrd.setText(text)
            msg = "Пароль скопирован!"
        else:
            msg = "Пароль ещё не сгенерирован или пуст!"
        self.show_informer(msg)

    def show_informer(self, text):
        informer = QtWidgets.QMessageBox()
        informer.setFixedSize(100, 100)
        informer.setWindowTitle("Password generator " + __version__)
        informer.setWindowIcon(QtGui.QIcon('key.png'))
        informer.setStandardButtons(QtWidgets.QMessageBox.Ok)
        informer.setDefaultButton(QtWidgets.QMessageBox.Ok)
        informer.setText(text)
        informer.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec_())
