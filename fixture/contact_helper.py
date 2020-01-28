class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def save_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # add firstname
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
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("aday", contact.aday)
        self.change_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create_contact(self, contact):
        wd = self.app.wd
        # add new address book
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_homepage()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()
        self.return_to_homepage()

    def edit_contact(self, contact):
        wd = self.app.wd
        self.return_to_homepage()
        # Edit
        # wd.find_element_by_xpath("//a[contains(@href,'Edit')]").click() - неправильно
        wd.find_element_by_css_selector("[id='maintable'] [name='entry'] td:nth-child(8) a img").click()
        # внести изменения
        self.fill_contact_form(contact)
        # update
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_homepage()
        # open modification form
        wd.find_element_by_css_selector("[id='maintable'] [name='entry'] td:nth-child(8) a img").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.return_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

