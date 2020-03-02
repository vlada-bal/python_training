from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/localhost") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) >0):
            wd.find_element_by_link_text("home").click()

    def save_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_days_and_months("bday", contact.bday)
        self.change_days_and_months("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_days_and_months("aday", contact.aday)
        self.change_days_and_months("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create_contact(self, contact):
        wd = self.app.wd
        # add new address book
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_homepage()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_homepage()
        # select first contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_contact(self, contact):
        wd = self.app.wd
        self.return_to_homepage()
        # Edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # внести изменения
        self.fill_contact_form(contact)
        # update
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_homepage()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_days_and_months(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        select = Select(wd.find_element_by_name(field_name))
        select.select_by_visible_text(text)
        wd.find_element_by_name(field_name).click()


    def count(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_homepage()
            self.contact_cache = []
            elements = wd.find_elements_by_css_selector("tr[name=entry]")
            for element in elements:
                firstname = element.find_elements_by_css_selector("td:nth-child(3)")[0].text
                lastname = element.find_elements_by_css_selector("td:nth-child(2)")[0].text
                address = element.find_elements_by_css_selector("td:nth-child(4)")[0].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_elements_by_css_selector("td:nth-child(6)")[0].text
                all_emails = element.find_elements_by_css_selector("td:nth-child(5)")[0].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.return_to_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        firstname=wd.find_element_by_name("firstname").get_attribute("value")
        lastname=wd.find_element_by_name("lastname").get_attribute("value")
        id=wd.find_element_by_name("id").get_attribute("value")
        homephone=wd.find_element_by_name("home").get_attribute("value")
        mobilephone=wd.find_element_by_name("mobile").get_attribute("value")
        workphone=wd.find_element_by_name("work").get_attribute("value")
        home2phone=wd.find_element_by_name("phone2").get_attribute("value")
        email1=wd.find_element_by_name("email").get_attribute("value")
        email2=wd.find_element_by_name("email2").get_attribute("value")
        email3=wd.find_element_by_name("email3").get_attribute("value")
        address=wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=homephone, mobile=mobilephone, work=workphone, phone2=home2phone,
                       email=email1, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.return_to_homepage()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        home2phone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, mobile=mobilephone, work=workphone, phone2=home2phone)

    def contact_add_to_group(self, group, id):
        wd = self.app.wd
        self.return_to_homepage()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        #wd.find_elements_by_id(contact_id).click()
        wd.find_element_by_name("to_group").click()
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_visible_text(group.name)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//input[@value='Add to']").click()

    def remove_contact_from_group(self, group):
         wd = self.app.wd
         self.return_to_homepage()
         select = Select(wd.find_element_by_name("group"))
         select.select_by_visible_text(group.name)
         wd.find_element_by_name("group").click()
         wd.find_element_by_name("remove").click()