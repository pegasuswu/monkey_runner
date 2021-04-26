import sys
# -*- coding: UTF-8 -*-
import time

from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer


if __name__ == '__main__':

    screenShotPath = 'd:/app_test/image/'
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    logPath = "d:/app_test/monkeyrunner/"
    log = open(logPath+"-log-"+now+".txt", "w")
    print("This is a simple monkeyrunner test script")


    device = mr.waitForConnection(30, 'AYG5T19328001569')
    log.write("wait for mobile phone connecting...、\n")
    device.startActivity(component=' com.cmcc.cmvideo/.splash.SplashActivity')
    log.write("start migu video\n")

    mr.sleep(10)


    log.write("click sports channel\n")
    device.touch(330, 2169, "DOWN_AND_UP")
    mr.sleep(5)

    log.write("click to china soccer channel\n")
    device.touch(496, 953, "DOWN_AND_UP")
    mr.sleep(5)


    log.write("click the search box\n")
    device.touch(320, 130, "DOWN_AND_UP")
    mr.sleep(2)
    device.type("first")
    device.press("KEYCODE_SPACE", "DOWN_AND_UP")
    device.type("blood")

    mr.sleep(2)
    device.touch(988, 130, "DOWN_AND_UP")
    log.write("wait for search results\n")
    mr.sleep(7)

    log.write("save image of searching result\n")
    resultImage = device.takeSnapshot()
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    resultImage.writeToFile(screenShotPath + "-search_result".decode("utf-8") + now + ".png", "png")
    print("Take a picture")


    log.write("click back button\n")
    device.press("KEYCODE_BACK", "DOWN_AND_UP")
    mr.sleep(3)
    device.press("KEYCODE_BACK", "DOWN_AND_UP")
    mr.sleep(3)
    device.press("KEYCODE_BACK", "DOWN_AND_UP")
    mr.sleep(3)
    device.press("KEYCODE_BACK", "DOWN_AND_UP")
    log.close()
    print('test complete,tks')
