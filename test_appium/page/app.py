"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/15 4:23 下午'
"""


# app.py 启动app， 重启，关闭
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 复用driver ,提升执行测试用例的速度
            print("driver == None,创建driver")
            caps = {}
            caps["platformName"] = "Android"
            # caps['skipDeviceInitialization'] = True
            # 包名+启动页名
            # mac/linux：adb logcat ActivityManager:I  | grep "cmp"
            # windows: adb logcat ActivityManager:I  | findstr "cmp"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["noReset"] = "True"
            caps["ensureWebviewsHavePages"] = True
            # 动态的设置caps 参数
            caps['settings[waitForIdleTimeout]'] = 0
            # 与server 建立连接，并且打开 caps 里面配置的页面LaunchSplashActivity
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 隐式等待,在调用所有的find_element /find_elements方法的时候被激活
            self.driver.implicitly_wait(5)
        else:
            print("复用driver")
            # 启动app
            self.driver.launch_app()
            # self.driver.start_activity()
        return self

    def restart(self):
        # 关闭
        self.driver.close()
        # 启动app
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self)->MainPage:
        # 入口
        return MainPage(self.driver)
