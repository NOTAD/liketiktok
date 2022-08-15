# Required packages
# pyinstaller   @pip install pyinstaller
# uiautomator2  @pip install --upgrade --pre uiautomator2

import json
import uiautomator2 as u2
from uiautomator2 import Direction
import requests
import configparser
import module
import time
from time import sleep

config = configparser.ConfigParser()
config.read('config.ini')
app = config['DEFAULT']['APP']
# device_passlock = config['DEFAULT']['DEVICE_PASSLOCK']
# app_passlock = config['DEFAULT']['APP_PASSLOCK']
# get_job_url = config['DEFAULT']['GET_JOB_URL']
# update_job_url = config['DEFAULT']['UPDATE_JOB_URL']


def init_device():
    d = u2.connect_usb()
    # Lauch the VCB app
    d.press("home")
    d.app_start(app)
    pid = d.app_wait(app)
    if not pid:
        print("Can not open")
        return False
    else:
        print("Mo ung dung thanh cong!")
        return d
def likeTiktok():
    # device.swipe_ext("up", scale=0.8)
    device.swipe_ext(Direction.FORWARD) # truot xuong
    device.implicitly_wait(2.0)
    try:
        getLike = device(resourceId=app+":id/agq").get_text()
    except:
        return 0
    realLike = module.unitToNumber(getLike)
    print("Cal Like: " +  realLike)
    if int(realLike) > 200000:
        device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/agp"]').click()
        time.sleep(10)
        return 1

if __name__ == '__main__':
    try:
        device = init_device()
        device.set_fastinput_ime(False)
        luotLike = 10 #So lan muon like tiktok
        start = 1
        while(start < luotLike):
            result = likeTiktok()
            if result == 1:
                start += 1
                print('Lan like thu: ' + str(start))

    except Exception as err:
        print(str(err))    