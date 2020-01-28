from model.group import Group

def test_delete_first_group(app):
    if app.group_helper.count() == 0:
        app.group_helper.creation(Group(name="test"))
    app.group_helper.delete_first_group()
