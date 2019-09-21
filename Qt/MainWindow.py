# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mousey.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 240)
        MainWindow.setMinimumSize(QtCore.QSize(220, 240))
        MainWindow.setMaximumSize(QtCore.QSize(220, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_mouse = QtWidgets.QCheckBox(self.centralwidget)
        self.click_mouse.setGeometry(QtCore.QRect(20, 20, 54, 54))
        self.click_mouse.setStyleSheet("QCheckBox {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px;\n"
"    height: 54px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/graphics/icons/click.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/graphics/icons/click-act.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/graphics/icons/click-hov.png);\n"
"}")
        self.click_mouse.setText("")
        self.click_mouse.setObjectName("click_mouse")
        self.hold_mouse = QtWidgets.QCheckBox(self.centralwidget)
        self.hold_mouse.setGeometry(QtCore.QRect(20, 80, 54, 54))
        self.hold_mouse.setStyleSheet("QCheckBox {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px;\n"
"    height: 54px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/graphics/icons/hold.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/graphics/icons/hold-act.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/graphics/icons/hold-hov.png);\n"
"}")
        self.hold_mouse.setText("")
        self.hold_mouse.setObjectName("hold_mouse")
        self.main_switch = QtWidgets.QCheckBox(self.centralwidget)
        self.main_switch.setGeometry(QtCore.QRect(20, 140, 180, 68))
        self.main_switch.setStyleSheet("QCheckBox {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 180px;\n"
"    height: 68px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/graphics/icons/switch.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/graphics/icons/switch-act.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/graphics/icons/switch-hov.png);\n"
"}")
        self.main_switch.setText("")
        self.main_switch.setObjectName("main_switch")
        self.comboBox_click = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_click.setGeometry(QtCore.QRect(80, 20, 120, 54))
        self.comboBox_click.setStyleSheet("QComboBox {    \n"
"    background-color: rgb(55, 72, 66);\n"
"    color: white;\n"
"    border-radius: 14px;\n"
"    font: 11pt \"Ubuntu\";\n"
"}\n"
"\n"
"QComboBox:hover {    \n"
"    background-color: rgb(58, 85, 75);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    background-color: rgb(108, 141, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(58, 85, 75);\n"
"    border: none;\n"
"}")
        self.comboBox_click.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_click.setIconSize(QtCore.QSize(42, 42))
        self.comboBox_click.setFrame(False)
        self.comboBox_click.setObjectName("comboBox_click")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/graphics/icons/Keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_hold = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_hold.setGeometry(QtCore.QRect(80, 80, 120, 54))
        self.comboBox_hold.setStyleSheet("QComboBox {    \n"
"    background-color: rgb(55, 72, 66);\n"
"    color: white;\n"
"    border-radius: 14px;\n"
"    font: 11pt \"Ubuntu\";\n"
"}\n"
"\n"
"QComboBox:hover {    \n"
"    background-color: rgb(58, 85, 75);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    background-color: rgb(108, 141, 250);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(58, 85, 75);\n"
"    border: none;\n"
"}")
        self.comboBox_hold.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_hold.setIconSize(QtCore.QSize(42, 42))
        self.comboBox_hold.setFrame(False)
        self.comboBox_hold.setObjectName("comboBox_hold")
        self.comboBox_hold.addItem(icon, "")
        self.comboBox_hold.addItem(icon, "")
        self.comboBox_hold.addItem(icon, "")
        self.comboBox_hold.addItem(icon, "")
        self.comboBox_hold.addItem(icon, "")
        self.comboBox_hold.addItem(icon, "")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-200, -300, 501, 591))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("border-image: url(:/icons/background5.png);")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.background.raise_()
        self.click_mouse.raise_()
        self.hold_mouse.raise_()
        self.main_switch.raise_()
        self.comboBox_click.raise_()
        self.comboBox_hold.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mousey"))
        self.comboBox_click.setItemText(0, _translate("MainWindow", "Shift-R"))
        self.comboBox_click.setItemText(1, _translate("MainWindow", "Shift"))
        self.comboBox_click.setItemText(2, _translate("MainWindow", "Ctrl"))
        self.comboBox_click.setItemText(3, _translate("MainWindow", "Alt"))
        self.comboBox_click.setItemText(4, _translate("MainWindow", "Ctrl-R"))
        self.comboBox_click.setItemText(5, _translate("MainWindow", "Alt-gr"))
        self.comboBox_hold.setItemText(0, _translate("MainWindow", "Shift-R"))
        self.comboBox_hold.setItemText(1, _translate("MainWindow", "Shift"))
        self.comboBox_hold.setItemText(2, _translate("MainWindow", "Ctrl"))
        self.comboBox_hold.setItemText(3, _translate("MainWindow", "Alt"))
        self.comboBox_hold.setItemText(4, _translate("MainWindow", "Ctrl-R"))
        self.comboBox_hold.setItemText(5, _translate("MainWindow", "Alt-gr"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
