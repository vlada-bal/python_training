# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    group = Group(name="kokoko", header="nehodite", footer="daleko")
    app.group_helper.creation(group)
    app.session.logout()

def test_add_empty_group(app):
     app.session.login(username="admin", password="secret")
     group = Group(name="", header="", footer="")
     app.group_helper.creation(group)
     app.session.logout()