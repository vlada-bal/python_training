# -*- coding: utf-8 -*-#
import pytest
from model.contact import Contact

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                                   company="", address="", home="", mobile="", work="", fax="",
                                                   email="", email2="", email3="", homepage="", bday="", bmonth="-",
                                                   byear="", aday="",
                                                   amonth="-", ayear="", address2="", phone2="", notes="")

    app.contact_helper.create_contact(contact)
    app.contact_helper.save_contact()
    app.session.logout()

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    contact = Contact(firstname="Firskatze", middlename="Middlekatze", lastname="Lasthund", nickname="Nickhund",
                      title="Titlehamster",
                      company="DobbiTelecom", address="Frankfurt am Main", home="7458232", mobile="+79111234545",
                      work="tester", fax="shmax",
                      email="qw@qw.qw", email2="we@we.we", email3="er@er.er", homepage="pagehome", bday="20",
                      bmonth="February", byear="1917", aday="17",
                      amonth="July", ayear="1864", address2="kokokotown", phone2="kokokohome", notes="notes shmotes")
    app.contact_helper.create_contact(contact)
    app.contact_helper.save_contact()
    app.session.logout()


