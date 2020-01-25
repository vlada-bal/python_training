from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group2 import GroupHelper

from fixture.contact_helper import ContactHelper
from selenium.webdriver.support.ui import Select

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group2 = GroupHelper(self)
        self.contact_helper = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()
