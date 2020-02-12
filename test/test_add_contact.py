# -*- coding: utf-8 -*-#
import pytest
from model.contact import Contact
from model.contact import Monate
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata= [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                                   company="", address="", home="", mobile="", work="", fax="",
                                                   email="", email2="", email3="", homepage="", bday="", bmonth="-",
                                                   byear="", aday="",
                                                   amonth="-", ayear="", address2="", phone2="", notes="")] + [
           Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                   lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                   title=random_string("title", 10), company=random_string("company", 10),
                   address=random_string("address", 10), home=random_string("home", 10),
                   mobile=random_string("mobile", 10), work=random_string("work", 10), fax=random_string("fax", 10),
                   email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
                   homepage=random_string("homepage", 10), bday=str(random.randint(1,27)), bmonth=Monate[random.randint(0,11)],
                   byear=random.randint(1600,2027), aday=str(random.randint(1,27)), amonth=Monate[random.randint(0,11)],
                   ayear=random.randint(1600,2027), address2=random_string("address2", 10), phone2=random_string("phone2", 10),
                   notes=random_string("notes", 10))
]
@pytest.mark.parametrize ("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_empty_contact(app, contact):
    old_contact = app.contact_helper.get_contact_list()
    app.contact_helper.create_contact(contact)
    app.contact_helper.save_contact()
    new_contact = app.contact_helper.get_contact_list()
    assert len(old_contact) + 1 == app.contact_helper.count ()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

# def test_add_contact(app):
#     old_contact = app.contact_helper.get_contact_list()
#     contact = Contact(firstname="Firskatze", middlename="Middlekatze", lastname="Lasthund", nickname="Nickhund",
#                       title="Titlehamster",
#                       company="DobbiTelecom", address="Frankfurt am Main", home="7458232", mobile="+79111234545",
#                       work="tester", fax="shmax",
#                       email="qw@qw.qw", email2="we@we.we", email3="er@er.er", homepage="pagehome", bday="20",
#                       bmonth="February", byear="1917", aday="17",
#                       amonth="July", ayear="1864", address2="kokokotown", phone2="kokokohome", notes="notes shmotes")
#     app.contact_helper.create_contact(contact)
#     app.contact_helper.save_contact()
#     new_contact = app.contact_helper.get_contact_list()
#     assert len(old_contact) + 1 == len(new_contact)
#     old_contact.append(contact)
#     assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



