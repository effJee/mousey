from layout import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    keyIndexList = [0, 1, 2, 3, 4, 5]

    # Linux keys scancodes
    keysDict = {"Shift": 50,
                "Ctrl": 37,
                "Alt": 64,
                "Shift-R": 62,
                "Ctrl-R": 105,
                "Alt-R": 108}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Slots and signals
        self.comboBox_hold.currentTextChanged.connect(self.holdComboBoxChanged)
        self.comboBox_click.currentTextChanged.connect(self.clickComboBoxChanged)
        self.click_mouse.toggled.connect(self.checkBoxToggled)
        self.hold_mouse.toggled.connect(self.checkBoxToggled)
        self.main_switch.toggled.connect(self.checkBoxToggled)

        self.clickHotkey = self.comboBox_click.currentText()
        self.holdHotkey = self.comboBox_hold.currentText()

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

    def keyPressEvent(self, event):
        keyScancode = event.nativeScanCode()

        if keyScancode == self.keysDict[self.clickHotkey]:
            print("Gruby idz spac")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
