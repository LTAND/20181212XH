# -*- coding: UTF-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()

if not device:
    print('device is not connected')
else:
    print('start')
    comand="com.hy.HoneyMarket/com.hy.HoneyMarket.processView.view.activity.RecyclerViewPagerActivity"
    device.startActivity(component=comand)
    MonkeyRunner.sleep(4)
    
    # 点击 小企鹅乐园下载
    device.touch(524,493,'DOWN_AND_UP')
    print('download')
    
    # 点击下载任务列表按钮
    MonkeyRunner.sleep(2)
    device.touch(1183,660,'DOWN_AND_UP')
    # device.takeSnapshot().writeToFile('D://1.png','png')

    # 删除下载任务
    MonkeyRunner.sleep(4)
    for i in range(1,5):
        device.touch(1127,278,'DOWN_AND_UP')
        MonkeyRunner.sleep(2)
    # device.takeSnapshot().writeToFile('D://2.png','png')

    # 退出 应用市场
    MonkeyRunner.sleep(3)
    (device.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP))*2