from model.group import Group

def test_modify_group_name(app):
    group = Group(name="New group")
    app.group_helper.modify_first_group(group)

def test_modify_group_header(app):
    group = Group(header="New Header")
    app.group_helper.modify_first_group(group)
