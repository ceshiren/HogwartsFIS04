"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/5/11 8:53 下午'
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# pip install appium-python-client
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class TestWX:
    def setup_class(self):
        self.fake = Faker('zh_CN')

    def setup(self):
        # 初始化
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

    def teardown(self):
        # 资源消毁
        self.driver.quit()

    def test_demo(self):
        # 测试用例
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView")

        el1.click()
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]/android.widget.LinearLayout/android.widget.TextView")
        el2.click()

    def test_daka(self):
        # 打卡功能
        # 前提条件
        # 已登录状态（ noReset = True）
        # 打卡用例：
        # 1、打开【企业微信】应用
        # 2、进入【工作台】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 3、点击【打卡】
        # 滚动查找 [打卡]
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().text("打卡")'
                                 '.instance(0));').click()
        # self.driver.update_settings({'waitForIdleTimeout':0})
        # 4、选择【外出打卡】tab
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 5、点击【第N次打卡】
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        # 6、验证【外出打卡成功】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        # 7、退出【企业微信】应用

    def swipe_find(self, text):
        num = 3
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                ele= self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele
            except:
                print("未找到")
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get('width')
                height = size.get("height")

                startx = width / 2
                starty = height * 0.8
                endx = startx
                endy = height * 0.3
                duration = 2000  # 单位是ms

                self.driver.swipe(startx, starty, endx, endy, duration)

            if i == 2:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException()


    def test_addcontact(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find("添加成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # find_elements 返回元素列表[element1,element2,element3.....]
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']").send_keys(phonenum)
        # self.driver.find_elements(MobileBy.XPATH, '//*[@text="必填"]')[1]
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        # WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@text='成功']"))
        # self.driver.find_element(MobileBy.CLASS_NAME, "android.widget.Toast")#.get_attribute('text')
        # print(result)
        # assert result == '添加成功'
        # sleep(2)
        # 获取页面的源代码
        # print(self.driver.page_source)
