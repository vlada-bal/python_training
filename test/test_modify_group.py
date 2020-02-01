from model.group import Group

def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.creation(Group(name="test"))
    old_groups = app.group_helper.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group_helper.modify_first_group(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
 #   if app.group_helper.count() == 0:
  #      app.group_helper.creation(Group(header="headertest"))
   # old_groups = app.group_helper.get_group_list()
    #group = Group(header="New Header")
#
 #   app.group_helper.modify_first_group(group)
  #  new_groups = app.group_helper.get_group_list()
   # assert len(old_groups) == len(new_groups)
    #old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

