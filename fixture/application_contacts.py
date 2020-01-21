from selenium import webdriver
from fixture.session_contacts import SessionContactsHelper
from fixture.group_for_contact2 import ContactsHelper
from selenium.webdriver.support.ui import Select


class Application_con:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contacts = SessionContactsHelper(self)
        self.group_for_contacts2 = ContactsHelper(self)

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()