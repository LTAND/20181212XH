# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()

if not device:
    print('devices is not connected')
else:
    print('start')
    comand="com.hy.storyMachine/.view.activity.HomeActivity"
    device.startActivity(component=comand)
    MonkeyRunner.sleep(4)
    # 播放 暂停
    device.touch(1155,616,'DOWN_AND_UP')
    MonkeyRunner.sleep(4)
    device.touch(1176,622,'DOWN_AND_UP')
    MonkeyRunner.sleep(3)
    # 下一首
    device.touch(1114,466,'DOWN_AND_UP')
    MonkeyRunner.sleep(3)
    # 上一首
    device.touch(996,557,'DOWN_AND_UP')