import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_baidu
from functools import partial

import requests
import json
import time


def fanyi(ui):

    url= 'https://fanyi.baidu.com/multitransapi'

    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        }

    #ui.textEdit.clear()

    input = ui.textEdit.toPlainText()
    coent = input

    data = {
        'from': 'en',
        'to': 'zh',
        'query': coent,
        'source': 'txt'
    }

    respos = requests.post(url,data,headers=headers).json()

    result = (respos['data']['cands'][0])

    ui.textEdit_2.setPlainText(str(result))
    

def qk(ui):
    ui.textEdit.clear()


 #array5 = array1.copy() # 对原始的array1的复制



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_baidu.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(partial(fanyi, ui))


    sys.exit(app.exec_())



