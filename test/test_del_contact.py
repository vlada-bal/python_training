from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact_helper.create_contact(Contact(firstname="del_con"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact_helper.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) -1 == len(new_contact)
    old_contact.remove(contact)
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)