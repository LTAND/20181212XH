#  -*- coding: UTF-8 -*-
import random
import os
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import By
device = MonkeyRunner.waitForConnection()

def startActivity(comand):
  # 启动activity
  activity = 'com.android.functiontest/'+comand
  device.startActivity(component=activity)
  MonkeyRunner.sleep(1)
  return 

def touchNext():
# 点击下一步按钮
  MonkeyRunner.sleep(1)
  device.touch(636,645,"DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  return

# ================lcp start=================
def testLcp():
  def doLcp():
    # 点击1次，切换不同颜色屏幕
    device.touch(298,140,"DOWN_AND_UP")
    MonkeyRunner.sleep(1)
    return 
  def doMoreLcp():
    # 点击7次，切换不同颜色屏幕
    for i in range(1,8):
      doLcp()
    print('lcp success')
    return 
  doMoreLcp()
  return 
# ================lcp end===================

# ==============屏幕亮度测试 start===========
def testBright():
  device.drag((1227,365),(68,365),0.1,10) # 0%亮度
  MonkeyRunner.sleep(3)
  device.drag((68,365),(1227,365),0.1,10) # 100%亮度
  print('bright success')
  return
# ================屏幕亮度测试 end============

# ================TP测试 start================
def testTp(len):
  # len -- 划线次数
  # 获取随机不超过屏幕的x,y坐标
  totalX = 1280
  totalY = 720
  def getPotX():
    return random.randint(0,totalX)
  def getPotY():
    return random.randint(0,totalY)

  def doLine():
    # 单次划线
    device.drag((getPotX(),getPotY()),(getPotX(),getPotY()),0.1,10)
    MonkeyRunner.sleep(1)
    return

  def doMoreLine(len):
    # 多次划线 -- len次数
    for i in range(1,len+1):
      print("doLine"+str(i))
      doLine()
    MonkeyRunner.sleep(1)
    print('TP success')
    return

  doMoreLine(len)
  return
# ================TP测试 end================


# ================WIFI测试 start============
def testWifi():
  # 打开网页
  touchNext()
  MonkeyRunner.sleep(5)
  print('WIFI success')
  return
# ================WIFI测试 end===============


# ================摄像头测试 start==============
def testCamera():
  # 拍照按钮
  MonkeyRunner.sleep(3)
  device.touch(1153,359,"DOWN_AND_UP")
  # 删除照片
  MonkeyRunner.sleep(5)
  device.touch(1153,470,"DOWN_AND_UP")
  print('camera success')
  return 
# ================摄像头测试 end================

# ================录音测试 start============
def testRecord():
  # 开始录音按钮
  device.touch(535,430,"DOWN_AND_UP")
  MonkeyRunner.sleep(10)
  device.touch(723,430,"DOWN_AND_UP")
  print('record success')
  return
  # 结束录音按钮
# ================录音测试 end==============

# ================音量测试 start==============
def testVolume():
  device.drag((1227,365),(68,365),0.1,10) # 0%音量
  MonkeyRunner.sleep(3)
  device.drag((68,365),(388,365),0.1,10) # 28%音量
  # device.drag((68,365),(1227,365),0.1,10) # 100%音量
  print('volume success')  
  return
# ================音量测试 end================


# ================行走测试 start==========
def testWalk():
  device.touch(624,173,"DOWN_AND_UP") # 前进
  MonkeyRunner.sleep(3)
  device.touch(624,482,"DOWN_AND_UP") # 停止
  return
# ================行走测试 end============

test = {
# testApp的一些Activity
  "main":".ui.MainActivity",
  "lcp":'.ui.LCDActivity',
  "tcp":".ui.TPActivity",
  "camera":".ui.CameraActivity",
  "record":".ui.RecordActivity"
}
def testApp():
  # 每个方法对应一个测试app的功能
  # touchNext() ---  点击下一步
  startActivity(test['main'])

  device.touch(298,140,"DOWN_AND_UP") 
  MonkeyRunner.sleep(1)
  testLcp()

  touchNext()
  testBright()

  touchNext()
  testTp(10) # 参数 -- 划线次数
  
  touchNext()
  testWifi()

  startActivity(test['camera'])
  testCamera()

  touchNext()
  # testRecord() # 录音自动化测试有问题，会自动崩溃
  
  touchNext()
  testVolume()

  touchNext()  # 下一步为按键功能测试
  return 

if __name__ == '__main__':
  # 录音, 蓝牙，按键，行走，呼吸灯测试就不自动化测试
  testApp()