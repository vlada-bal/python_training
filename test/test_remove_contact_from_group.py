from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1',
                             name='addressbook',
                             user='root',
                             password='')

def test_remove_contact_from_group(app, check_ui):
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact_helper.create_contact(Contact(firstname="el_contacto"))

    if len(db.get_group_list()) == 0:
        app.group_helper.creation(Group(name="test"))

    group_list = db.get_group_list()
    group = group_list[0]

    contacts_in_group = db.get_contacts_in_group(group)

    if len(contacts_in_group) == 0:
        app.contact_helper.contact_add_to_group(group)
    app.contact_helper.remove_contact_from_group(group)