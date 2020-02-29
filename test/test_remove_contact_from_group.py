from model.contact import Contact
from model.group import Group
import random


def test_contact_add_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact_helper.create_contact(Contact(firstname="el_contacto"))
    if len(db.get_group_list()) == 0:
        app.group_helper.creation(Group(name="test"))
    app.contact_helper.contact_add_to_group()
    if :
        app.contact_helper.contact_add_to_group()