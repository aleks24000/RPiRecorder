import sys
import subprocess
from PyQt5 import QtWidgets
from RecUI import Ui_MainWindow
from RPiFunctions import start, stop_rec, upload_file
from gpiozero import Button
from signal import pause
from RPiFunctions import startFromGui
from RPiFunctions import stopFromGui
from RPiFunctions import upload_file
from threading import Thread

ex = None

def screenoff():
    subprocess.call('DISPLAY=:0 xset dpms force off', shell=True)


def startGui():
    subprocess.call('DISPLAY=:0 xset dpms force on', shell=True)
    global ex
    ex.pushButton.setStyleSheet("background-color: red")
    startFromGui()

def stopGui():
    subprocess.call('DISPLAY=:0 xset dpms force on', shell=True)
    global ex
    ex.pushButton_2.setStyleSheet("background-color: red")
    stopFromGui()
    ex.pushButton.setStyleSheet("background-color: green")
    ex.pushButton_2.setStyleSheet("background-color: green")

def uploadGui():
    subprocess.call('DISPLAY=:0 xset dpms force on', shell=True)
    global ex
    ex.pushButton_3.setStyleSheet("background-color: red")
    thread = Thread(target = upload_file)
    thread.start()
    #upload_file()
    ex.pushButton_3.setStyleSheet("background-color: green")


if __name__ == "__main__":
    global ex
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)

    button = Button(12)
    button_stop = Button(20)
    button_upload = Button(26)
    button_screen = Button(16)

    button.when_pressed = startGui
    button_stop.when_pressed = stopGui
    button_upload.when_pressed = uploadGui
    button_screen.when_pressed = screenoff

    w.show()

    #pause()
    #startGui(ex)
    #ex.pushButton.setStyleSheet("background-color: red")
    sys.exit(app.exec_())
    #app.exec_()
    print("exiting")
