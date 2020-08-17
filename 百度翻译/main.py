import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_baidu import Ui_MainWindow
import requests
import json
import execjs
import re
import os




class baidufanyi(QMainWindow,Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.fanyi)       
        self.pushButton_2.clicked.connect(self.fuzhi)
        self.pushButton_3.clicked.connect(self.clear)

        #实例化剪切板
        self.clipboard = QApplication.clipboard()
   
 
    def get_sign(self,query):

        #path=os.path.abspath('.')   #表示当前所处的文件夹的绝对路径
        with open('baidu.js','r', encoding='utf-8') as f:
            ctx = execjs.compile(f.read())
        sign = ctx.call('e', query)
        return sign
   


    def fanyi(self):

        query = self.textEdit.toPlainText()
        sign = self.get_sign(query)

        url= 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59',
            'cookie': 'BAIDUID=6F8C4E12FC561D8D1B338F6F345CC743:FG=1; BIDUPSID=6F8C4E12FC561D8D1B338F6F345CC743; PSTM=1595585591; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1596683310,1596683483,1597580042,1597590073; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1597592518; __yjsv5_shitong=1.0_7_b0bbc2ee594fe2238715fd746a485a1aa451_300_1597592518006_218.84.240.187_74d65e0e; yjs_js_security_passport=7f7410780dbd6794fe1fe71f6be572f24c19d74a_1597592518_js'
            }

        content = '[\u4e00-\u9fa5]'
        res = re.findall(content,query)

        #判断输入英文啊还是中文
        if res:
       
            data = {

                "from": "zh",
                "to": "en",
                "query": query,  # query 即我们要翻译的的内容
                "transtype": "realtime",
                "simple_means_flag": "3",
                "sign": sign,  # sign 是变化的需要我们执行js代码得到
                "token": "fe60ae6381b8b5aec69478b595b07f60",
                'domain': 'common'
            }

        else:
            data = {

                "from": "en",
                "to": "zh",
                "query": query,  # query 即我们要翻译的的内容
                "transtype": "realtime",
                "simple_means_flag": "3",
                "sign": sign,  # sign 是变化的需要我们执行js代码得到
                "token": "fe60ae6381b8b5aec69478b595b07f60",
                'domain': 'common'
            }

        respose = requests.post(url,data=data,headers=headers).json()
        
        result = respose['trans_result']['data'][0]['dst']

        self.textEdit_2.setPlainText(str(result))
       

    #复制功能实现
    def fuzhi (self):
        self.clipboard.setText(self.textEdit_2.toPlainText())

    #清空
    def clear(self):
        self.textEdit_2.setText("")
        self.textEdit.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    myWin = baidufanyi()
    myWin.show()

    sys.exit(app.exec_())





