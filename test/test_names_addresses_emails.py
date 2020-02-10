import re
from random import randrange


def test_emails_on_home_page(app):
    index = randrange(len(app.contact_helper.get_contact_list()))
    contact_from_home_page = app.contact_helper.get_contact_list()[index]
    contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    # скливание всех емейлов со страницы редактирования
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x), filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3]))))

def test_last_names_on_home_page(app):
     index = randrange(len(app.contact_helper.get_contact_list()))
     contact_from_home_page = app.contact_helper.get_contact_list()[index]
     contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
     assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
#
def test_first_names_on_home_page(app):
     index = randrange(len(app.contact_helper.get_contact_list()))
     contact_from_home_page = app.contact_helper.get_contact_list()[index]
     contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
     assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)

def test_addresses_on_home_page(app):
     index = randrange(len(app.contact_helper.get_contact_list()))
     contact_from_home_page = app.contact_helper.get_contact_list()[index]
     contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
     assert contact_from_home_page.address == contact_from_edit_page.address