from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_contact(Contact(firstname="del_con"))
    old_contact = app.contact_helper.get_contact_list()
    index = randrange(len(old_contact))
    app.contact_helper.delete_contact_by_index(index)
    new_contact = app.contact_helper.get_contact_list()
    assert len(old_contact) -1 == len(new_contact)

    old_contact[index:index+1] = []
    assert old_contact == new_contact