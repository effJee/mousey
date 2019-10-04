from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets
from layout import Ui_MainWindow

from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput import keyboard

import pyautogui

# import threading
import time
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    keyIndexList = [0, 1, 2, 3, 4, 5]

    # Custom signals
    clickSignal = pyqtSignal()
    holdSignal = pyqtSignal()

    # Key scancodes
    keysDict = {"Shift": Key.shift_l,
                "Ctrl": Key.ctrl_l,
                "Alt": Key.alt_l,
                "Shift-R": Key.shift_r,
                "Ctrl-R": Key.ctrl_r,
                "Alt-R": Key.alt_r}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.listener = keyboard.Listener(on_release=self.keyPressed)
        self.listener.start()

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

    def keyPressed(self, key):

        if key == self.keysDict[self.clickHotkey]:
            self.clickSignal.emit()

        if key == self.keysDict[self.holdHotkey]:
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
                self.mouse.click(Button.left)
                # pyautogui.click(button='left')
                # print("clicking")
                # time.sleep(.100)
            elif window.hold_active and not self.pressed:
                self.mouse.press(Button.left)
                # print("Pressed")
                self.pressed = True
            elif self.pressed and not window.hold_active:
                self.mouse.release(Button.left)
                # print("Realsed")
                self.pressed = False
            time.sleep(.100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    worker = WorkerThread()
    worker.start()
    window.show()
    app.exec()
