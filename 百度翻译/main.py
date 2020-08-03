import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Ui_baidu import Ui_MainWindow

import requests
import json
import time



class baidufanyi(QMainWindow,Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.fanyi)
        
        self.pushButton_2.clicked.connect(self.fuzhi)

        #if not self.textEdit_2.setPlainText:
        #self.pushButton.returnPressed.connect(self.fanyi)

        #实例化剪切板
        self.clipboard = QApplication.clipboard()  


    def fanyi(self):

        url= 'https://fanyi.baidu.com/multitransapi'

        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
            }

        #ui.textEdit.clear()

        input = self.textEdit.toPlainText()
        coent = input

        data = {
            'from': 'en',
            'to': 'zh',
            'query': coent,
            'source': 'txt'
        }

        respos = requests.post(url,data,headers=headers).json()

        result = (respos['data']['cands'][0])

        self.textEdit_2.setPlainText(str(result))



    #复制功能实现
    def fuzhi (self):
        self.clipboard.setText(self.textEdit_2.toPlainText())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    myWin = baidufanyi()
    myWin.show()


    sys.exit(app.exec_())





