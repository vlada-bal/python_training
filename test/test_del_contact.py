from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_contact(Contact(firstname="del_con"))
    old_contact = app.contact_helper.get_contact_list()
    app.contact_helper.delete_first_contact()
    new_contact = app.contact_helper.get_contact_list()
    assert len(old_contact) -1 == len(new_contact)


    old_contact[0:1] = []
    assert old_contact == new_contact