from model.contact import Contact
from selenium.webdriver.support.ui import Select

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
        wd.find_element_by_name("selected[]").click()
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

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_homepage()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill group form
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
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)

