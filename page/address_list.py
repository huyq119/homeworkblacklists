from appium.webdriver.common.mobileby import MobileBy

import page.add_contact
from page.base_page import BasePage


class AddressList(BasePage):

    def goto_add_contact(self):
        self.find_click((MobileBy.ID, "com.tencent.wework:id/idp"))
        return page.add_contact.Add_Contact(self._driver)