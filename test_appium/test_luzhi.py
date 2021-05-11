"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/11 8:51 下午'
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
# 不建议使用录制出来的代码
# 1、格式需要优化
# 2、定位器生成的太复杂
# 3、没有断言
caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["deviceName"] = "hogwarts"
caps["noReset"] = "True"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]/android.widget.LinearLayout/android.widget.TextView")
el2.click()

driver.quit()