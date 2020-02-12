# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata= [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range (5)
]

#testdata= [Group(name=name, header=header, footer=footer)
 #          for name in ["", random_string("name", 10)]
  #         for header in ["", random_string("header", 20)]
   #        for footer in ["", random_string("footer", 20)]]

@pytest.mark.parametrize ("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group_helper.get_group_list()
    app.group_helper.creation(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) + 1 == app.group_helper.count()
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
