from model.contact import Contact

def test_modify_contact_company(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_contact(Contact(company="Tiboshek"))
    contact = Contact(company="New company")
    app.contact_helper.modify_first_contact(contact)

def test_modify_contact_nickname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_contact(Contact(nickname="Nushanja"))
    contact = Contact(nickname="New Nickname")
    app.contact_helper.modify_first_contact(contact)