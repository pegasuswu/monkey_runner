 # OverView
The monkeyrunner tool provides an API for writing programs that control an Android device or emulator from outside of Android code. With monkeyrunner, you can write a Python program that installs an Android application or test package, runs it, sends keystrokes to it, takes screenshots of its user interface, and stores screenshots on the workstation. The monkeyrunner tool is primarily designed to test applications and devices at the functional/framework level and for running unit test suites.
## Working environment
**Jdk、Python、Android SDK**.  
The aboving enquirements need to be installed firstly.There are lots of instructions available online.
## Get the main activity name
**adb shell pm list packages |grep video**  
The command gets all the package which contains 'video'.Select the test object app.  
**pm list packages|grep video**  
package:com.qiyi.video  
package:com.sohu.sohuvideo.emplayer  
package:com.huawei.videoeditor  
package:com.fengshows.video  
package:com.cmvideo.migumovie  
package:com.huawei.multimedia.hivideoplayengine  
package:com.cmcc.cmvideo  
package:com.ss.android.article.video  
Here selected app is  com.cmcc.cmvideo:
**adb shell dumpsys com.cmcc.cmvideo**.   
In the output window,find the Launcher activity:com.cmcc.cmvideo/.splash.SplashActivity filter 83f51a Action: "android.intent.action.MAIN"
Category: "android.intent.category.LAUNCHER"
So device.startActivity(component='**com.cmcc.cmvideo/.splash.SplashActivity**')
## Get the specific location
monkeryrunner d:\XX\XX\monkey_recorder.py.Then it will display the main window,From the window We can get the position of some specific location  
## Writing script
screenShotPath = 'd:/app_test/image/'  
now = time.strftime("%Y_%m_%d_%H_%M_%S")  
logPath = "d:/app_test/monkeyrunner/"  
log = open(logPath+"-log-"+now+".txt", "w")  
print("This is a simple monkeyrunner test script") 
## use adb devices get the device id
device = mr.waitForConnection(30, 'AYG5T19328001569')  
log.write("wait for mobile phone connecting...、\n")  
device.startActivity(component=' com.cmcc.cmvideo/.splash.SplashActivity')  
log.write("start migu video\n")  
mr.sleep(10)  
  
log.write("click sports channel")  
device.touch(330, 2169, "DOWN_AND_UP")  
mr.sleep(5)  

log.write("click to china soccer channel")  
device.touch(496, 953, "DOWN_AND_UP")  
mr.sleep(5)  

log.write("click the search box")  
device.touch(320, 130, "DOWN_AND_UP")  
mr.sleep(2)  
device.type("first")  
device.press("KEYCODE_SPACE", "DOWN_AND_UP")  
device.type("blood")  
  
mr.sleep(2)  
device.touch(988, 130, "DOWN_AND_UP")  
log.write("wait for search results")  
mr.sleep(7)  
  
log.write("save image of searching result")  
resultImage = device.takeSnapshot()  
now = time.strftime("%Y-%m-%d-%H-%M-%S")  
resultImage.writeToFile(screenShotPath + "-search_result".decode("utf-8") + now + ".png", "png")  
print("Take a picture")  
  
  
log.write("click back button\n")  
device.press("KEYCODE_BACK", "DOWN_AND_UP")  
mr.sleep(3)  
  
log.close()  
print('test complete,tks')

## Run the script
From command line:
monkeyrunner  d:\XX\XX\test_scripts.py
Then the script will begin to work.
### SyntaxError: Non-ASCII Character
The reason is that we should indicate this in front of monkeyrunner scripts.
#-*- coding: UTF-8 -*-
