def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact_helper.delete_first_contact()
    app.session.logout()