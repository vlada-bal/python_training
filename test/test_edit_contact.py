from model.contact import Contact

def test_edit_contact(app):
    contact = Contact(firstname="Firskatze_", middlename="Middlekatze_", lastname="Lasthund_", nickname="Nickhund_",
                      title="Titlehamster_",
                      company="DobbiTelecom_", address="Frankfurt am Main_", home="7458232_", mobile="+79111234545_",
                      work="tester_", fax="shmax_",
                      email="qw@qw.qw_", email2="we@we.we_", email3="er@er.er_", homepage="pagehome_", bday="20",
                      bmonth="February", byear="1918", aday="18",
                      amonth="July", ayear="1865", address2="kokokotown_", phone2="kokokohome_", notes="notes shmotes_")

    app.contact_helper.edit_contact(contact)
