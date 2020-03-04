from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1',
                             name='addressbook',
                             user='root',
                             password='')

def test_contact_add_to_group(app, check_ui):
# проверяем что есть вообще контакт и группа
    if len(db.get_contact_list()) == 0:
        app.contact_helper.create_contact(Contact(firstname="el_contacto"))
    if len(db.get_group_list()) == 0:
        app.group_helper.creation(Group(name="test"))

    group_list = db.get_group_list()
    has_contacts_not_in_group = False

   # old_list = db.get_contacts_in_group()

# получаем контакты, которые не в группе
    for i in range(len(group_list)):
        group = group_list[i]
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        # если существуют контакты, которые не в группе, то мы берем 1й контакт и добавляем в группу
        if (len(contacts_not_in_group) > 0):
            app.contact_helper.contact_add_to_group(group, contacts_not_in_group[0].id)
            has_contacts_not_in_group = True
            break

# если все контакты во всех группах, то создаём новый котакт и связываем его с группой
    if has_contacts_not_in_group is not True:
        new_contact = Contact(firstname="el_contacto", id="666")
        app.contact_helper.create_contact(new_contact)
        app.contact_helper.contact_add_to_group(group, new_contact.id)

    #new_list = db.get_contacts_in_group()
# проверка на то, что добавили контакт в группу
   # assert len(old_list)+1 == len(new_list)

