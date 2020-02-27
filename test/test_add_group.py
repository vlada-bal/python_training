# -*- coding: utf-8 -*-
from model.group import Group



#testdata= [Group(name=name, header=header, footer=footer)
 #          for name in ["", random_string("name", 10)]
  #         for header in ["", random_string("header", 20)]
   #        for footer in ["", random_string("footer", 20)]]

def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group_helper.creation(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group_helper.get_group_list()
    group = Group(name="", header="", footer="")
    app.group_helper.creation(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
