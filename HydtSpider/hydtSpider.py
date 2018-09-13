import requests
from bs4 import BeautifulSoup
import time
import emailSender
# import ctypes


urls = [
    # 龙岩地区
        # "http://www.zpsfdc.com/",      # 漳平
        "http://www.fjlyfdc.com.cn/",  # 龙岩
        "http://www.wpxfdc.com.cn/",    # 武平

        # 南平地区
        "http://222.78.249.228:81/",    # 顺昌
        "http://www.wysfgc.com/",       # 武夷山
        "http://222.78.251.53/?tdsourcetag=s_pctim_aiomsg",     # 光泽
        "http://www.pcfgs.com/",        # 浦城
        "http://www.jofwdj.com/",       # 建瓯
        "http://www.jyfdc.com/",        # 建阳

        # 宁德地区
        "http://www.fafgj.com/Content/xw_hydt",        # 福安
        # "http://www.fdfdc.cn/",         # 福鼎

        # 莆田地区
        "http://www.fjxyfdc.com/",      # 仙游

        # # 泉州地区
        "http://www.nafdc.com.cn/?COLLCC=2688041923&",  # 南安

        # 三明地区

        "http://www.dtfgs.com/",        # 大田
        "http://www.fjsxfdc.com/",      # 沙县
        # "http://www.nhfdc.com.cn/",     # 宁化
        "http://218.86.116.222/"        # 尤溪
]
 

class HydtSpider():
    def __init__(self):
        self.urls = urls
        self.result = []
        self.hydt_date = ''
        self.email_subject = ''
        self.segme = '\r\n'
        self.current_date = ''
        self.current_date_MD = ''

    def request(self, url):
        r = requests.get(url)
        return r

    def crawl(self):
        for url in self.urls:
            html = self.request(url)
            html.encoding = 'utf-8'
            soup = BeautifulSoup(html.text, 'lxml').select("#HYDTprey li span")

            # 判断网页上行业动态人的日期是否为空
            if soup:         
                self.hydt_date = soup[0].text # 获取第一条信息的日期，和今天的日期做对比
            else:
                self.hydt_date = "请求网站无法正常打开，请检查！"

            self.current_date = time.strftime("%Y-%m-%d", time.localtime())
            self.current_date_MD = time.strftime("%m-%d", time.localtime())

            if self.hydt_date == self.current_date or self.hydt_date == self.current_date_MD:
                print(url,"同步成功！")
            else:
                self.result.append(url + '  ' + self.hydt_date + '\r\n')
                    
    def sendEmailFun(self):  # 爬取结束的时候发送邮件
        # finishTime = datetime.datetime.now()
        # "1785381349@qq.com", "2955529716@qq.com"
        emailSenderClient = emailSender.emailSender()
        toSendEmailLst = ['3431295272@qq.com']
        subject = f"有{str(len(self.result))}个网站同步失败"
        body = f"以下网站行业动态同步失败：{self.segme.join(self.result)}"
        emailSenderClient.sendEmail(toSendEmailLst, subject, body)

    def save_text(self):
        with open('D:/HydtLog/'+ self.current_date + '.txt', 'a',encoding='utf8') as f: # 这里要加上 encoding='utf8' 不然写入文件后中文会乱码
            f.write(self.segme.join(self.result))

hydt_spider = HydtSpider()
hydt_spider.crawl()
hydt_spider.sendEmailFun()
hydt_spider.save_text()

# 弹窗
# ctypes.windll.user32.MessageBoxW(0, u'网站行业动态已全部检查完毕，结果保存在程序目录的hydt文件夹', u'检查结果',0)