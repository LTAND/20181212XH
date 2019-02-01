# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()

comand = 'com.huiyu.honeyrobot.car/.view.activity.OptionsMainActivity'
device.startActivity(component=comand)

MonkeyRunner.sleep(2)

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
MonkeyRunner.sleep(4)
for i in range(0, 14):
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
# 最后停留在用户管理页面
device.touch(92,72,"DOWN_AND_UP")