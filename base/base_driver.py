from appium import webdriver


def init_driver():
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.1'
    desired_caps['deviceName'] = '8a88ccdc'
    # app信息
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = 'com.tpshop.malls.SPMainActivity'
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # toast
    desired_caps['automationName'] = 'Uiautomator2'
    # 声明对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
