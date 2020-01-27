from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    group = Group(name="u koshki", header="tolstie", footer="nojki")
    app.group_helper.edit_group(group)
    app.session.logout()