import sys
import re
from datetime import datetime, date, time
from PyQt5 import QtWidgets, QtGui, QtCore
from timechangergui import Ui_MainWindow
from functions import get_files_path, time_to_seconds, change_files_modification_time, change_files_creation_time, get_mod_and_cr_time


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('other/icon.ico'))

        self.ui.textBrowser.setReadOnly(True)
        self.ui.textBrowser_2.setReadOnly(True)

        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.clearButton.clicked.connect(self.clearClicked)

        self.filenames = ()

        self.ui.dateTimeEdit.setDateTime(datetime.now())
        self.ui.dateTimeEdit_2.setDateTime(datetime.now())

        self.ui.applyButton_1.clicked.connect(self.apply1Clicked)
        self.ui.applyButton_2.clicked.connect(self.apply2Clicked)

        self.ui.resetButton.clicked.connect(self.reset1Clicked)
        self.ui.resetButton_2.clicked.connect(self.reset2Clicked)
        
        self.ui.applyAllButton.clicked.connect(self.apply1Clicked)
        self.ui.applyAllButton.clicked.connect(self.apply2Clicked)
        
        self.ui.resetAllButton.clicked.connect(self.reset1Clicked)
        self.ui.resetAllButton.clicked.connect(self.reset2Clicked)

    def btnClicked(self):
        self.filenames = get_files_path()
        self.ui.textBrowser.setText(str(self.filenames))
        self.ui.textBrowser_2.setText(str(get_mod_and_cr_time(self.filenames)))

    def clearClicked(self):
        self.filenames = ()
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()

    def apply1Clicked(self):
        self.dte = self.ui.dateTimeEdit.dateTime()
        self.dte = re.search(r'\(.+\)', str(self.dte))
        self.dt = str(self.dte.group(0))
        self.dt = self.dt.replace('(', '')
        self.dt = self.dt.replace(')', '')
        self.dateandtime = re.split(r',\s', self.dt)

        self.year = int(self.dateandtime[0])
        self.month = int(self.dateandtime[1])
        self.day = int(self.dateandtime[2])
        self.hour = int(self.dateandtime[3])
        self.minute = int(self.dateandtime[4])
        self.second = int(self.dateandtime[5])

        change_files_modification_time(time_to_seconds(
            self.month,
            self.day,
            self.year,
            self.hour,
            self.minute,
            self.second
        ), self.filenames)
        self.ui.textBrowser_2.setText(str(get_mod_and_cr_time(self.filenames)))

    def apply2Clicked(self):
        self.dte = self.ui.dateTimeEdit_2.dateTime()
        self.dte = re.search(r'\(.+\)', str(self.dte))
        self.dt = str(self.dte.group(0))
        self.dt = self.dt.replace('(', '')
        self.dt = self.dt.replace(')', '')
        self.dateandtime = re.split(r',\s', self.dt)

        self.year = int(self.dateandtime[0])
        self.month = int(self.dateandtime[1])
        self.day = int(self.dateandtime[2])
        self.hour = int(self.dateandtime[3])
        self.minute = int(self.dateandtime[4])
        self.second = int(self.dateandtime[5])

        change_files_creation_time(time_to_seconds(
            self.month,
            self.day,
            self.year,
            self.hour,
            self.minute,
            self.second
        ), self.filenames)
        self.ui.textBrowser_2.setText(str(get_mod_and_cr_time(self.filenames)))

    def reset1Clicked(self):
        self.ui.dateTimeEdit.setDateTime(datetime.now())

    def reset2Clicked(self):
        self.ui.dateTimeEdit_2.setDateTime(datetime.now())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
