import easygui as pic

import serial as ser

ser.baudrate = 9600
ser.port = 'COM3'

#print(ser)

while(1):
    YesorNO = pic.buttonbox("我是最牛逼的吗？", title="肯定时的", choices=  ['YES', 'NO', 'EXIT'])
    if YesorNO == 'EXIT':
       str = pic.enterbox("你的悄悄话", title="你的心里话")
       print(str)
    if YesorNO == 'YES':
        netx_ch = pic.multchoicebox("请选择我的优点",title="粉丝团",choices=['就是帅','狠帅','非常帅'])
        if netx_ch == '就是帅':
            print("666")
    else:
        break

