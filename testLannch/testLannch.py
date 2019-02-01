# -*- coding: UTF-8 -*-
import sys,os,re
from com.android.monkeyrunner import MonkeyDevice, MonkeyImage, MonkeyRunner

device = MonkeyRunner.waitForConnection()

def enterLannch():
  # ==========截图设置入口==========
  filePath = 'D://test_image'  
  imgPath = filePath+'/number.png'

  if not os.path.isdir(filePath):  
    # 该文件夹不存在，则创建
    os.makedirs(filePath)

  device.touch(53,53,"DOWN_AND_UP")   
  MonkeyRunner.sleep(5)
  device.takeSnapshot().writeToFile(imgPath,'png')
  print('sreenshots success')
  return True

def ocrImg(enterLannchFlag):
  if(enterLannchFlag):
    # 必须将项目放在d盘
    output = os.popen(r'D:\20181212XH\testLannch\baiduApi.py').read()  # 返回的是脚本打印结果
    print('ocrImg success')
    # print(output)
    if(output):
      results = []
      A = int(output)/10
      B = int(output)%10
      results.append(A)
      results.append(B)
      return results
    else:
      print('picture ocr is null')

def enter():
  # 自动输入验证码
  enterLannchFlag = enterLannch()
  nums = ocrImg(enterLannchFlag)
  for i in range(0, len(nums)): 
    if nums[i] ==1:
      device.touch(372,412,"DOWN_AND_UP") 
    elif nums[i]==2:
      device.touch(524,411,"DOWN_AND_UP") 
    elif nums[i]==3:
      device.touch(620,411,"DOWN_AND_UP")
    elif nums[i]==4:
      device.touch(792,411,"DOWN_AND_UP") 
    elif nums[i]==5:
      device.touch(956,411,"DOWN_AND_UP") 
    elif nums[i]==6:
      device.touch(328,552,"DOWN_AND_UP") 
    elif nums[i]==7:
      device.touch(492,552,"DOWN_AND_UP") 
    elif nums[i]==8:
      device.touch(632,552,"DOWN_AND_UP") 
    elif nums[i]==9:
      device.touch(820,552,"DOWN_AND_UP") 
    elif nums[i]==0:
      device.touch(952,552,"DOWN_AND_UP")
  return True

if(enter()):
  MonkeyRunner.sleep(5)
  # 进入lannchs
  # 锁屏唤醒 -- （默认是关闭状态） 
  device.touch(828,282,"DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  device.touch(713,217,"DOWN_AND_UP")
  MonkeyRunner.sleep(3)
  device.touch(713,217,"DOWN_AND_UP")
  device.touch(92,72,"DOWN_AND_UP")

  # 护眼设置
  MonkeyRunner.sleep(1)
  device.touch(1120,244,"DOWN_AND_UP")
  MonkeyRunner.sleep(5)
  for i in range(0, 15):
    device.touch(848,372,"DOWN_AND_UP")
  device.drag((331,595),(926,595),0.1,10) 
  MonkeyRunner.sleep(3)
  device.drag((926,595),(331,595),0.1,10)
  for i in range(0, 14):
    device.touch(416,378,"DOWN_AND_UP")
  MonkeyRunner.sleep(2)
  device.touch(92,72,"DOWN_AND_UP")

  # 时间设置 -- 自动同步
  MonkeyRunner.sleep(1)
  device.touch(484,522,"DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  device.touch(829,253,"DOWN_AND_UP")
  MonkeyRunner.sleep(2)
  device.touch(829,253,"DOWN_AND_UP")
  MonkeyRunner.sleep(2)
  device.touch(92,72,"DOWN_AND_UP")
  MonkeyRunner.sleep(1)
  
  # 最后停留在用户管理页面
  device.touch(477,246,"DOWN_AND_UP")
# print(type(nums))
# print(nums)
