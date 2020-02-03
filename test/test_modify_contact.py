from model.contact import Contact

def test_modify_contact_company(app):
    old_contact = app.contact_helper.get_contact_list()
    if app.contact_helper.count() == 0:
        app.contact_helper.create_contact(Contact(company="Tiboshek"))
    contact = Contact(company="Dunder Mifflin")
    app.contact_helper.modify_first_contact(contact)
    new_contact = app.contact_helper.get_contact_list()
    assert len(old_contact) == len(new_contact)

# def test_modify_contact_nickname(app):
  #  if app.contact_helper.count() == 0:
   #     app.contact_helper.create_contact(Contact(nickname="Nushanja"))
    #contact = Contact(nickname="New Nickname")
    #app.contact_helper.modify_first_contact(contact)