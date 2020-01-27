# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    group = Group(name="kokoko", header="nehodite", footer="daleko")
    app.group_helper.creation(group)

def test_add_empty_group(app):
     group = Group(name="", header="", footer="")
     app.group_helper.creation(group)
