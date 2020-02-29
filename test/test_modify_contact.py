from model.contact import Contact
from random import randrange

def test_modify_contact_company(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact_helper.create_contact(Contact(company="Tiboshek"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(company="Dunder Mifflin")
    contact.id = old_contact[index].id
    app.contact_helper.modify_contact_by_index(index, contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact_helper.create_contact(Contact(firstname="Nushanja"))
    old_contact = db.get_contact_list()
    contact = Contact(firstname="New York", id=old_contact[0].id)
    app.contact_helper.modify_first_contact(contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    if check_ui:
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
