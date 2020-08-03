import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication,QMainWindow
#导入designer工具生成的login模块
from Ui_vip import Ui_MainWindow
import webbrowser
import requests
from lxml import etree


class MyMainForm(QMainWindow,Ui_MainWindow):

    #url = 'http://www.wpsseo.cn/'
    url = "http://www.bt4kyy.com/yun/jiexi.php"
    headers = {
    
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
    
        }

    parse_url = requests.get(url=url,headers=headers)
    parse_url.encoding ='utf-8'
    get_html= parse_url.text

    tree = etree.HTML(get_html)

    jiexi_urls = tree.xpath("//*[@id='pgcontainer']//select")

# 获取vip解析名称
    for jiexi_name in jiexi_urls:
        jiexi_name = jiexi_name.xpath("./option/text()")
#获取vip解析地址
    for jiexi_url in jiexi_urls:
        jiexi_url = jiexi_url.xpath("./option/@value")

    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

 #开始逻辑层编写
 ## 信号   
     
        self.pushButton.clicked.connect(self.open_url)
        self.pushButton_2.clicked.connect(self.clear_url)

 
        self.radioButton.toggled.connect(self.parse_urls)
        self.radioButton_2.toggled.connect(self.parse_urls)
        self.radioButton_3.toggled.connect(self.parse_urls)

        #重新定义按钮名字
        self.radioButton.setText(self.jiexi_name[0])
        self.radioButton_2.setText(self.jiexi_name[1])
        self.radioButton_3.setText(self.jiexi_name[2])
        self.radioButton_4.setText(self.jiexi_name[3])
        self.radioButton_5.setText(self.jiexi_name[4])
        self.radioButton_6.setText(self.jiexi_name[5])



        #self.radioButton_4.toggled.connect(self.parse_url)
        
        self.radioButton.setChecked(True)


#清除输入框
    def clear_url(self):
        self.lineEdit.clear()

#打开浏览器输入地址
    def open_url(self):
        end_url = self.lineEdit.text()
        url = self.first_url + end_url

        webbrowser.open(url)

#定义信号源
    def parse_urls(self,jiexi_url):
        if self.radioButton.isChecked():
            self.first_url = self.jiexi_url[0]

        elif self.radioButton_2.isChecked():
            self.first_url = self.jiexi_url[1]

        elif self.radioButton_3.isChecked():
            self.first_url = self.jiexi_url[2]

        elif self.radioButton_4.isChecked():
            self.first_url = self.jiexi_url[3]

        elif self.radioButton_5.isChecked():
            self.first_url = self.jiexi_url[4]

        elif self.radioButton_6.isChecked():
            self.first_url = self.jiexi_url[5]


        #elif self.radioButton_4.isChecked():
            #self.first_url = self.jiexi_url[3]

   

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())





