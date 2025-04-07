from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if browserName == 'Firefox':
            return webdriver.Firefox()
        elif browserName == 'Chrome':
            return webdriver.Chrome()