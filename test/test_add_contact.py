# -*- coding: utf-8 -*-#
import pytest
from model.contact import Contact

def test_add_empty_contact(app):
    old_contact = app.contact_helper.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                                   company="", address="", home="", mobile="", work="", fax="",
                                                   email="", email2="", email3="", homepage="", bday="", bmonth="-",
                                                   byear="", aday="",
                                                   amonth="-", ayear="", address2="", phone2="", notes="")

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



