# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group_for_contact import Group_contact




class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.new_contact_creation(wd, Group_contact(firstname="", middlename="", lastname="", nickname="", title="",
                                  company="", address="", home="", mobile="", work="", fax="",
                                  email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="",
                                  amonth="-", ayear="", address2="", phone2="", notes=""))
        self.save_contact(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.new_contact_creation(wd, Group_contact(firstname="Firskatze", middlename="Middlekatze", lastname="Lasthund", nickname="Nickhund", title="Titlehamster",
                                  company="DobbiTelecom", address="Frankfurt am Main", home="7458232", mobile="+79111234545", work="tester", fax="shmax",
                                  email="qw@qw.qw", email2="we@we.we", email3="er@er.er", homepage="pagehome", bday="20", bmonth="February", byear="1917", aday="17",
                                  amonth="July", ayear="1864", address2="kokokotown", phone2="kokokohome", notes="notes shmotes"))
        self.save_contact(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):

        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):

        wd.find_element_by_link_text("home page").click()

    def save_contact(self, wd):

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def new_contact_creation(self, wd, Group_contact):
        # add new address book
        wd.find_element_by_link_text("add new").click()
        # add firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Group_contact.firstname)
        # add middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Group_contact.middlename)
        # add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Group_contact.lastname)
        # add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Group_contact.nickname)
        # add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Group_contact.title)
        # add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Group_contact.company)
        # add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Group_contact.address)
        # add home
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Group_contact.home)
        # add mobile
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Group_contact.mobile)
        # add work
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Group_contact.work)
        # add fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Group_contact.fax)
        # add email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Group_contact.email)
        # add email2
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Group_contact.email2)
        # add email3
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Group_contact.email3)
        # add homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Group_contact.homepage)
        # add Birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Group_contact.bday)
        wd.find_element_by_name("bday").click()
        # add month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Group_contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        # add yeahr
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Group_contact.byear)
        wd.find_element_by_name("theform").click()
        # add Anniversary day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Group_contact.aday)
        wd.find_element_by_name("aday").click()
        # add Anniversary month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Group_contact.amonth)
        wd.find_element_by_name("amonth").click()
        # add Anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Group_contact.ayear)
        # add address2
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Group_contact.address2)
        # add phone2
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Group_contact.phone2)
        # add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Group_contact.notes)

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/edit.php")

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/label[2]").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
