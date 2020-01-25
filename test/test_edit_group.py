




def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group_helper.edit_group()
    app.session.logout()