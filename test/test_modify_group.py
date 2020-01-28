from model.group import Group

def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.creation(Group(name="test"))
    group = Group(name="New group")
    app.group_helper.modify_first_group(group)

def test_modify_group_header(app):
    if app.group_helper.count() == 0:
        app.group_helper.creation(Group(header="headertest"))
    group = Group(header="New Header")
    app.group_helper.modify_first_group(group)
