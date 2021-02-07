from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.add_contact_option import Add_Contact_Option
from page.base_page import BasePage


class Contacts(BasePage):

    def goto_add_contact_option(self):
        """
        滑动查找元素
        :return:
        """
        self.roll_click("添加成员")
        return Add_Contact_Option(self._driver)

    def get_name_list(self):
        sleep(5)
        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/em4']"
                                   "//*[@class='android.widget.TextView']")
        element_list = WebDriverWait(self._driver, 10).until(expected_conditions.presence_of_all_elements_located(locator))
        name_list = []
        for element in element_list:
            name_list.append(element.text)
        return name_list
