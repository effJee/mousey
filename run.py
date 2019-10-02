from PyQt5.QtCore import QThread, pyqtSignal
from pynput.mouse import Button, Controller
from layout import Ui_MainWindow
from PyQt5 import QtWidgets
import threading
import pyautogui
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    keyIndexList = [0, 1, 2, 3, 4, 5]

    # Custom signals
    clickSignal = pyqtSignal()
    holdSignal = pyqtSignal()

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

        # Flags
        self.click_active = False
        self.hold_active = False
        self.main_on = False
        self.click_on = False
        self.hold_on = False

        # Current hotkey set
        self.clickHotkey = self.comboBox_click.currentText()
        self.holdHotkey = self.comboBox_hold.currentText()

        # Slots and signals
        self.comboBox_hold.currentTextChanged.connect(self.holdComboBoxChanged)
        self.comboBox_click.currentTextChanged.connect(self.clickComboBoxChanged)
        self.click_mouse.toggled.connect(self.clickCheckBoxToggled)
        self.hold_mouse.toggled.connect(self.holdCheckBoxToggled)
        self.main_switch.toggled.connect(self.mainCheckBoxToggled)
        self.clickSignal.connect(self.handleClickSignal)
        self.holdSignal.connect(self.handleHoldSignal)

    # ComboBox slot
    def clickComboBoxChanged(self):
        self.clickHotkey = self.comboBox_click.currentText()
        if self.clickHotkey == self.holdHotkey:
            # this way prevents from setting negative key index since
            # keyIndexList[-1] will give us the last list item
            newIndex = self.keyIndexList[self.comboBox_hold.currentIndex() - 1]
            self.comboBox_hold.setCurrentIndex(newIndex)

    # ComboBox slot
    def holdComboBoxChanged(self):
        self.holdHotkey = self.comboBox_hold.currentText()
        if self.holdHotkey == self.clickHotkey:
            # this way prevents from setting negative key index since
            # keyIndexList[-1] will give us the last list item
            newIndex = self.keyIndexList[self.comboBox_click.currentIndex() - 1]
            self.comboBox_click.setCurrentIndex(newIndex)

    def handleClickSignal(self):
        if self.main_on and self.click_on:
            self.hold_active = False
            self.click_active = not self.click_active

    def handleHoldSignal(self):
        if self.main_on and self.hold_on:
            self.click_active = False
            self.hold_active = not self.hold_active

    # ChecBox slots
    def mainCheckBoxToggled(self):
        self.main_on = not self.main_on
        if not self.main_on:
            self.click_active = False
            self.hold_active = False

    def clickCheckBoxToggled(self):
        self.click_on = not self.click_on
        if not self.click_on:
            self.click_active = False

    def holdCheckBoxToggled(self):
        self.hold_on = not self.hold_on
        if not self.hold_on:
            self.hold_active = False

    def keyPressEvent(self, event):
        keyScancode = event.nativeScanCode()

        if keyScancode == self.keysDict[self.clickHotkey]:
            self.clickSignal.emit()

        if keyScancode == self.keysDict[self.holdHotkey]:
            self.holdSignal.emit()


class WorkerThread(QThread):
    def __init__(self):
        super().__init__()
        self.mouse = Controller()
        self.pressed = False

    def run(self):
        print("Thread working!")
        # print(threading.currentThread().getName())
        while True:
            if window.click_active:
                """Hey, there"""
                # self.mouse.click(Button.left)
                # self.mouse.press(Button.left)
                # self.mouse.release(Button.left)
                # pyautogui.click()
            elif window.hold_active:
                # self.mouse.press(Button.left)
                self.pressed = True
                # time.sleep(1)
            elif self.pressed:
                # self.mouse.release(Button.left)
                self.pressed = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    worker = WorkerThread()
    worker.start()
    window.show()
    app.exec()
