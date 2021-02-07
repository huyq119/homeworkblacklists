from appium.webdriver.common.mobileby import MobileBy

import page.add_contact_option
from page.address_list import AddressList
from page.base_page import BasePage
from page.set_department import Set_Department
import page.message_contact_fail
from page.set_gender import Set_Gender


class Add_Contact(BasePage):

    def add_contact(self, _name, _phone, _gender):
        self.find_sendkeys((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ern']"
                                            "//*[@resource-id='com.tencent.wework:id/b78']"), _name)
        self.find_sendkeys((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f5y']"
                                            "//*[@resource-id = 'com.tencent.wework:id/fuy']"), _phone)
        self.goto_set_gender().set_gender(_gender)
        self.goto_address_list().goto_add_contact()
        # self.goto_set_department().set_department()
        self.find_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        return page.add_contact_option.Add_Contact_Option(self._driver)

    def add_contact_fail(self, _name, _phone, _gender):
        self.find_sendkeys((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ern']"
                                            "//*[@resource-id='com.tencent.wework:id/b78']"), _name)
        self.find_sendkeys((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f5y']"
                                            "//*[@resource-id = 'com.tencent.wework:id/fuy']"), _phone)
        self.goto_set_gender().set_gender(_gender)
        self.goto_address_list().goto_add_contact()
        # self.goto_set_department().set_department()
        self.find_click((MobileBy.ID, "com.tencent.wework:id/ie7"))
        return page.message_contact_fail.Message_Contact_Fail(self._driver)

    # def goto_set_department(self):
    #     self.find(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/er0']"
    #                               "//*[@resource-id='com.tencent.wework:id/b81']").click()
    #     return Set_Department(self._driver)

    def goto_set_gender(self):
        self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7a']/..//"
                                         "*[@resource-id='com.tencent.wework:id/b81']"))
        return Set_Gender(self._driver)

    def goto_address_list(self):
        self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/jr']"
                                         "//*[@resource-id='com.tencent.wework:id/b82']"))
        return AddressList(self._driver)
