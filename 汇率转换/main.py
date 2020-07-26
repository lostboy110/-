import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_fanyi
from functools import partial


def convert(ui):
    input = ui.lineEdit.text() 
    result1 = float(input) * 6.7
    ui.lineEdit_2.setText(str(result1))

  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_fanyi.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(partial(convert, ui))

    sys.exit(app.exec_())



