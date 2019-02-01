# -*- coding: UTF-8 -*-
import os
import re

# 获取设备的所有包列表
def getPackages():
  packages = []
  out = os.popen('adb shell pm list packages').read().replace("package:","")
  # 返回切割后数组
  res = re.split(r'\n',out)
  # 去空数组
  packages = list(filter(None, res))
  return packages

# 获取appList.txt的要检测的预安装列表
def getAppList():
  appList = []
  f = open(r'D:\20181212XH\appList.txt','r',encoding='utf-8')
  content = f.readlines()
  for line in content:
    appList.append(line.replace("\n", "").replace("package:",""))
  f.close()
  # 去除列表为空的回车
  return list(filter(None, appList)) 

print("****************预安装app检测开始****************")
count = 1
for a in getAppList():
  if(a not in getPackages()):
    print(count,"预安装app中没有:",a)
  else: 
    print(count,"check success")
  count+=1
print("****************预安装app检测完成****************")


