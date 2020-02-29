import re
from random import randrange
from model.contact import Contact

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    # скливание всех емейлов со страницы редактирования
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: str.strip(x), filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_on_home_page(contact):
    # скливание всех телефонов со страницы редактирования
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x), filter(lambda x: x is not None,
                            [contact.home, contact.mobile, contact.work, contact.phone2]))))

def test_assert_contacts(app, db, check_ui):
    contact_from_home_page = app.contact_helper.get_contact_list()
    contact_from_basa = db.get_contact_list()
    sorted_contacts_from_homepage = sorted(contact_from_home_page, key=Contact.id_or_max)
    sorted_contacts_from_basa = sorted(contact_from_basa, key=Contact.id_or_max)
    for i in range(len(sorted_contacts_from_homepage)):
        contact__homepage = sorted_contacts_from_homepage[i]
        contact__basa = sorted_contacts_from_basa[i]
        assert contact__homepage.lastname == str.strip(contact__basa.lastname)
        assert contact__homepage.firstname == str.strip(contact__basa.firstname)
        assert contact__homepage.address == str.strip(contact__basa.address)
        assert contact__homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact__basa)
        assert contact__homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact__basa)
