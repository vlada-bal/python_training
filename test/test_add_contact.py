# -*- coding: utf-8 -*-

import pytest
from model.contact import Group_contact


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.group_for_contacts2.creation(Group_contact(firstname="", middlename="", lastname="", nickname="", title="",
                                                   company="", address="", home="", mobile="", work="", fax="",
                                                   email="", email2="", email3="", homepage="", bday="", bmonth="-",
                                                   byear="", aday="",
                                                   amonth="-", ayear="", address2="", phone2="", notes=""))
    app.group_for_contacts2.save_contact()
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group_for_contacts2.creation(
        Group_contact(firstname="Firskatze", middlename="Middlekatze", lastname="Lasthund", nickname="Nickhund",
                      title="Titlehamster",
                      company="DobbiTelecom", address="Frankfurt am Main", home="7458232", mobile="+79111234545",
                      work="tester", fax="shmax",
                      email="qw@qw.qw", email2="we@we.we", email3="er@er.er", homepage="pagehome", bday="20",
                      bmonth="February", byear="1917", aday="17",
                      amonth="July", ayear="1864", address2="kokokotown", phone2="kokokohome", notes="notes shmotes"))
    app.group_for_contacts2.save_contact()
    app.session.logout()


