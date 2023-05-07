# -*- coding: utf-8 -*-
# @Time : 2020/5/10 21:45
# @Author : ZS
# @Site : 
# @File : serial_post.py
# @Software: PyCharm

import serial
import requests
import time
import json
import serial.tools.list_ports
from lxml import etree
class Data_su():
    def __init__(self):
            self.post_data = {}
            self.get_data = None
            self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}

    def Post_data(self):
        print('post')
        print(self.post_data)# 使用post访问服务器，并且携带数据发送
        # 访问网址的时候需要带上个人的id，便于下发指令和显示数据，方便登录使用，进行权限查看
        # response = requests.post('http://www.tianqiapi.com/api?version=v9&appid=23035354&appsecret=8YvlPNrz',
        #                          data=self.data,headers=self.header)
        session = requests.session()
        response = session.get('http://127.0.0.1:8000/news/luntan',headers=self.header)
        html = etree.HTML(response.content.decode())  # 使用xpath解析
        csrf = html.xpath('/html/body/section/div/div/input/@value')[0]  # 获取csrf值
        self.post_data['csrfmiddlewaretoken']=csrf#向字典中动态添加元素
        print(self.post_data)
        response = session.post('http://127.0.0.1:8000/datas/data_receive',
                                 data=self.post_data, headers=self.header)
        datas = response.content.decode()# 接收返回的数据
        print(response)
        data = json.loads(datas)
        self.get_data = data['code'] # 获取具体指令操作
        print(self.get_data)

    def Get_data(self):  # 获得lora数据
        print('get')
        try:
            port_list = list(serial.tools.list_ports.comports())# 搜索串口，获取串口
            print(port_list[0][0])
            if len(port_list) == 0:
                return
            else:
                # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
                portx = port_list[0][0]
                # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
                bps = 9600
                # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
                # 打开串口，并得到串口对象
                ser = serial.Serial(portx, bps, timeout=500)
                print("串口详情参数：", ser)
                while True:
                    if ser.in_waiting:
                        str = ser.read(ser.in_waiting).decode('gbk')
                        print(str)
                        self.post_data = {
                            'wendu': str[5:10].strip(),# 温度
                            'shidu': str[13:18].strip(),# 湿度
                            'oxgen': 600,# 二氧化碳
                            'shui': 66 # 土壤湿度
                        }
                        print(self.post_data)
                        data_su.Post_data()
                        print(self.get_data)#这里验证返回值是否是on或者off
                        if self.get_data == 'off':
                            ser.write(chr(0x01).encode("utf-8"))
                            print('write is ok')
                        if self.get_data == 'on':
                            ser.write(chr(0x10).encode("utf-8"))
                        ser.close()
                        time.sleep(30)
                        return
        except:
            print('请插入串口设备')
            time.sleep(30)# 当没有设备或者服务器没有响应，都会触发

if __name__ == '__main__':
    while True:
        data_su = Data_su()

        data_su.Get_data()


