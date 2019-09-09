from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    click_on = False
    hold_on = False
    mainSwitch_on = False

    clickHotkey = ""
    holdHotkey = ""

    keyIndexList = [0, 1, 2, 3, 4, 5]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 240)
        MainWindow.setMinimumSize(QtCore.QSize(220, 240))
        MainWindow.setMaximumSize(QtCore.QSize(220, 240))

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Autoclick button (checkbox)
        self.click_mouse = QtWidgets.QCheckBox(self.centralwidget)
        self.click_mouse.setGeometry(QtCore.QRect(20, 20, 54, 54))
        self.click_mouse.setStyleSheet("QCheckBox {\n"
                                       "    background-color: none;\n"
                                       "}\n"
                                       "QCheckBox::indicator {\n"
                                       "    width: 54px;\n"
                                       "    height: 54px;\n"
                                       "}\n"
                                       "QCheckBox::indicator:unchecked {\n"
                                       "    image: url(./icons/click.png);\n"
                                       "}\n"
                                       "QCheckBox::indicator:checked {\n"
                                       "    image: url(./icons/click-act.png);\n"
                                       "}\n"
                                       "QCheckBox::indicator:unchecked:hover {\n"
                                       "    image: url(./icons/click-hov.png);\n"
                                       "}")
        self.click_mouse.setText("")
        self.click_mouse.setObjectName("click_mouse")

        # Hold button (checkbox)
        self.hold_mouse = QtWidgets.QCheckBox(self.centralwidget)
        self.hold_mouse.setGeometry(QtCore.QRect(20, 80, 54, 54))
        self.hold_mouse.setStyleSheet("QCheckBox {\n"
                                      "    background-color: none;\n"
                                      "}\n"
                                      "QCheckBox::indicator {\n"
                                      "    width: 54px;\n"
                                      "    height: 54px;\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked {\n"
                                      "    image: url(./icons/hold.png);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "    image: url(./icons/hold-act.png);\n"
                                      "}\n"
                                      "QCheckBox::indicator:unchecked:hover {\n"
                                      "    image: url(./icons/hold-hov.png);\n"
                                      "}")
        self.hold_mouse.setText("")
        self.hold_mouse.setObjectName("hold_mouse")

        # On/off switch (checkbox)
        self.main_switch = QtWidgets.QCheckBox(self.centralwidget)
        self.main_switch.setGeometry(QtCore.QRect(20, 140, 180, 68))
        self.main_switch.setStyleSheet("QCheckBox {\n"
                                       "    background-color: none;\n"
                                       "}\n"
                                       "QCheckBox::indicator {\n"
                                       "    width: 180px;\n"
                                       "    height: 68px;\n"
                                       "}\n"
                                       "QCheckBox::indicator:unchecked {\n"
                                       "    image: url(./icons/switch.png);\n"
                                       "}\n"
                                       "QCheckBox::indicator:checked {\n"
                                       "    image: url(./icons/switch-act.png);\n"
                                       "}\n"
                                       "QCheckBox::indicator:unchecked:hover {\n"
                                       "    image: url(./icons/switch-hov.png);\n"
                                       "}")
        self.main_switch.setText("")
        self.main_switch.setObjectName("main_switch")

        # Autoclick hotkey selection list (combobox)
        self.comboBox_click = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_click.setGeometry(QtCore.QRect(80, 20, 120, 54))
        self.comboBox_click.setStyleSheet("QComboBox {    \n"
                                          "    background-color: rgb(55, 72, 66);\n"
                                          "    color: white;\n"
                                          "    border-radius: 14px;\n"
                                          "    font: 11pt \"Ubuntu\";\n"
                                          "}\n"
                                          "QComboBox:hover {    \n"
                                          "    background-color: rgb(58, 85, 75);\n"
                                          "    color: white;\n"
                                          "    border-radius: 15px;\n"
                                          "}\n"
                                          "QComboBox:on {\n"
                                          "    background-color: rgb(108, 141, 250);\n"
                                          "}\n"
                                          "QComboBox::drop-down {\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "QComboBox QAbstractItemView {\n"
                                          "    background-color: rgb(58, 85, 75);\n"
                                          "    border: none;\n"
                                          "}")
        self.comboBox_click.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_click.setIconSize(QtCore.QSize(42, 42))
        self.comboBox_click.setFrame(False)
        self.comboBox_click.setObjectName("comboBox_click")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/Keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.addItem(icon, "")
        self.comboBox_click.setCurrentIndex(2)  # Left alt key

        # Hold hotkey selection list (combobox)
        self.comboBox_hold = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_hold.setGeometry(QtCore.QRect(80, 80, 120, 54))
        self.comboBox_hold.setStyleSheet("QComboBox {    \n"
                                         "    background-color: rgb(55, 72, 66);\n"
                                         "    color: white;\n"
                                         "    border-radius: 14px;\n"
                                         "    font: 11pt \"Ubuntu\";\n"
                                         "}\n"
                                         "QComboBox:hover {    \n"
                                         "    background-color: rgb(58, 85, 75);\n"
                                         "    color: white;\n"
                                         "    border-radius: 15px;\n"
                                         "}\n"
                                         "QComboBox:on {\n"
                                         "    background-color: rgb(108, 141, 250);\n"
                                         "}\n"
                                         "QComboBox::drop-down {\n"
                                         "    border: none;\n"
                                         "}\n"
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

        # Slots and signals
        self.comboBox_hold.currentTextChanged.connect(self.holdComboBoxChanged)
        self.comboBox_click.currentTextChanged.connect(self.clickComboBoxChanged)
        self.click_mouse.toggled.connect(self.checkBoxToggled)
        self.hold_mouse.toggled.connect(self.checkBoxToggled)
        self.main_switch.toggled.connect(self.checkBoxToggled)

        # Background
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-200, -300, 501, 591))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("border-image: url(./icons/background.png);")
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

    # ComboBox slots
    def clickComboBoxChanged(self):
        self.clickHotkey = self.comboBox_click.currentText()
        print("Click: ", self.clickHotkey)
        if self.clickHotkey == self.holdHotkey:
            # this way prevents from setting negative key index since
            # keyIndexList[-1] will give us the last list item
            newIndex = self.keyIndexList[self.comboBox_hold.currentIndex() - 1]
            self.comboBox_hold.setCurrentIndex(newIndex)

    def holdComboBoxChanged(self):
        self.holdHotkey = self.comboBox_hold.currentText()
        print("Hold: ", self.holdHotkey)
        if self.holdHotkey == self.clickHotkey:
            # this way prevents from setting negative key index since
            # keyIndexList[-1] will give us the last list item
            newIndex = self.keyIndexList[self.comboBox_click.currentIndex() - 1]
            self.comboBox_click.setCurrentIndex(newIndex)

    # CheckBox slots
    def checkBoxToggled(self):
        if self.click_mouse.isChecked():
            self.click_on = True
        else:
            self.click_on = False

        if self.hold_mouse.isChecked():
            self.hold_on = True
        else:
            self.hold_on = False

        if self.main_switch.isChecked():
            self.mainSwitch_on = True
        else:
            self.mainSwitch_on = False

        print("Click: ", self.click_on)
        print("Hold: ", self.hold_on)
        print("Switch: ", self.mainSwitch_on)
        print("--------")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mousey"))
        self.comboBox_click.setItemText(0, _translate("MainWindow", "Shift"))
        self.comboBox_click.setItemText(1, _translate("MainWindow", "Ctrl"))
        self.comboBox_click.setItemText(2, _translate("MainWindow", "Alt"))
        self.comboBox_click.setItemText(3, _translate("MainWindow", "Shift-R"))
        self.comboBox_click.setItemText(4, _translate("MainWindow", "Ctrl-R"))
        self.comboBox_click.setItemText(5, _translate("MainWindow", "Alt-R"))
        self.comboBox_hold.setItemText(0, _translate("MainWindow", "Shift"))
        self.comboBox_hold.setItemText(1, _translate("MainWindow", "Ctrl"))
        self.comboBox_hold.setItemText(2, _translate("MainWindow", "Alt"))
        self.comboBox_hold.setItemText(3, _translate("MainWindow", "Shift-R"))
        self.comboBox_hold.setItemText(4, _translate("MainWindow", "Ctrl-R"))
        self.comboBox_hold.setItemText(5, _translate("MainWindow", "Alt-R"))


def on_release(key):
    global clickHotkey_active
    global holdHotkey_active

    if ui.mainSwitch_on:

        if ui.click_on:
            if key == hotkeysDict[ui.clickHotkey]:
                if not clickHotkey_active:
                    clickHotkey_active = True
                    holdHotkey_active = False
                else:
                    clickHotkey_active = False
                print("Click: ", clickHotkey_active)
                print("Hold: ", holdHotkey_active)

        if ui.hold_on:
            if key == hotkeysDict[ui.holdHotkey]:
                if not holdHotkey_active:
                    holdHotkey_active = True
                    clickHotkey_active = False
                else:
                    holdHotkey_active = False
                print("Click: ", clickHotkey_active)
                print("Hold: ", holdHotkey_active)
                print(".......")


if __name__ == "__main__":
    from pynput.mouse import Button, Controller
    from pynput import keyboard
    import sys

    hotkeysDict = {"Shift": keyboard.Key.shift_l,
                   "Ctrl": keyboard.Key.ctrl_l,
                   "Alt": keyboard.Key.alt_l,
                   "Shift-R": keyboard.Key.shift_r,
                   "Ctrl-R": keyboard.Key.ctrl_r,
                   "Alt-R": keyboard.Key.alt_r}

    clickHotkey_active = False
    holdHotkey_active = False

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    mouse = Controller()

    sys.exit(app.exec_())
