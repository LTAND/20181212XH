# -*- coding: UTF-8 -*-
import os
import re

# 获取设备的所有包列表
packages = []
out = os.popen('adb shell pm list packages').read().replace("package:","")
# 返回切割后数组
res = re.split(r'\n',out)
# 去空数组
packages = list(filter(None, res))
# print(packages)

# 获取appList.txt的要检测的预安装列表
appList = []
f = open(r'D:\20181212XH\appList.txt','r',encoding='utf-8')
content = f.readlines()
for line in content:
  appList.append(line.replace("\n", "").replace("package:",""))
f.close()
# print(appList)

print("****************预安装app检测开始****************")
count = 1
for a in appList:
  if(a not in packages):
    print(count,"预安装app中没有:",a)
  else: 
    print(count,"success")
  count+=1
print("****************预安装app检测完成****************")


