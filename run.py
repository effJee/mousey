from PyQt5.QtCore import QThread, pyqtSignal
from pynput.mouse import Button, Controller
from layout import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import time


class WorkerThread(QThread):
    def __init__(self):
        super().__init__()
        self.mouse = Controller()
        self.click_active = False
        self.hold_active = False
        self.main_on = False
        self.click_on = False
        self.hold_on = False

    def handleClickSignal(self):
        if self.main_on and self.click_on:
            self.hold_active = False
            self.click_active = not self.click_active

        print("********")
        print("Hold: ", self.hold_active)
        print("Click: ", self.click_active)
        print("********")

    def handleHoldSignal(self):
        if self.main_on and self.hold_on:
            self.click_active = False
            self.hold_active = not self.hold_active

            # if self.hold_active:
            #     self.mouse.press(Button.left)
            #     print("Pressed!")
            # else:
            #     self.mouse.release(Button.left)
            #     print("Released!")

        print("********")
        print("Hold: ", self.hold_active)
        print("Click: ", self.click_active)
        print("********")

    def mainCheckBoxToggled(self):
        self.main_on = not self.main_on
        if not self.main_on:
            self.click_on = False
            self.hold_on = False
        print("main on: ", self.main_on)

    def clickCheckBoxToggled(self):
        self.click_on = not self.click_on
        if not self.click_on:
            self.click_active = False
        print("click on: ", self.click_on)

    def holdCheckBoxToggled(self):
        self.hold_on = not self.hold_on
        if not self.hold_on:
            self.hold_active = False
        print("hold on: ", self.hold_on)

    def run(self):
        print("Thread working!")
        # while True:
        #     if self.click_active and self.main_on:
        #         # self.mouse.click(Button.left)
        #         print("clicking!")
        #         time.sleep(2)
        #     elif self.hold_active and self.main_on:
        #         # self.mouse.press(Button.left)
        #         print("pressing!")
        #         time.sleep(2)
        #     elif not self.hold_active and self.main_on:
        #         # self.mouse.release(Button.left)
        #         print("releasing!")
        #         time.sleep(2)
        # while True:
        #     print("...")
        #     if self.hold_active:
        #         break

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    clickSignal = pyqtSignal()
    holdSignal = pyqtSignal()
    keyIndexList = [0, 1, 2, 3, 4, 5]

    # Linux key scancodes
    keysDict = {"Shift": 50,
                "Ctrl": 37,
                "Alt": 64,
                "Shift-R": 62,
                "Ctrl-R": 105,
                "Alt-R": 108}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.clickHotkey = self.comboBox_click.currentText()
        self.holdHotkey = self.comboBox_hold.currentText()
        self.worker = WorkerThread()
        self.worker.start()

        # Slots and signals
        self.comboBox_hold.currentTextChanged.connect(self.holdComboBoxChanged)
        self.comboBox_click.currentTextChanged.connect(self.clickComboBoxChanged)
        self.click_mouse.toggled.connect(self.worker.clickCheckBoxToggled)
        self.hold_mouse.toggled.connect(self.worker.holdCheckBoxToggled)
        self.main_switch.toggled.connect(self.worker.mainCheckBoxToggled)
        self.clickSignal.connect(self.worker.handleClickSignal)
        self.holdSignal.connect(self.worker.handleHoldSignal)

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
    # def checkBoxToggled(self):
    #     if self.click_mouse.isChecked():
    #         self.click_on = True
    #     else:
    #         self.click_on = False
    #
    #     if self.hold_mouse.isChecked():
    #         self.hold_on = True
    #     else:
    #         self.hold_on = False
    #
    #     if self.main_switch.isChecked():
    #         self.mainSwitch_on = True
    #     else:
    #         self.mainSwitch_on = False
    #
    #     print("Click: ", self.click_on)
    #     print("Hold: ", self.hold_on)
    #     print("Switch: ", self.mainSwitch_on)
    #     print("--------")

    def keyPressEvent(self, event):
        keyScancode = event.nativeScanCode()

        if keyScancode == self.keysDict[self.clickHotkey]:
            print("click click")
            self.clickSignal.emit()

        if keyScancode == self.keysDict[self.holdHotkey]:
            print("hold hold")
            self.holdSignal.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
