def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group_helper.delete_first_group()
    app.session.logout()