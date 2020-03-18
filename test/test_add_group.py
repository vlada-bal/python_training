# -*- coding: utf-8 -*-
from model.group import Group
import allure

# def test_add_group(app, db, json_groups, check_ui):
#     group = json_groups
#     old_groups = db.get_group_list()
#     app.group_helper.creation(group)
#     new_groups = db.get_group_list()
#     old_groups.append(group)
#     if check_ui:
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step("When I add a group %s to the list" % group):
        app.group_helper.creation(group)
    with allure.step('Then the new group list equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#testdata= [Group(name=name, header=header, footer=footer)
 #          for name in ["", random_string("name", 10)]
  #         for header in ["", random_string("header", 20)]
   #        for footer in ["", random_string("footer", 20)]]
#
# def test_add_empty_group(app, db, check_ui):
#     old_groups = db.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group_helper.creation(group)
#     new_groups = db.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     if check_ui:
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
