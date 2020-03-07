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

# делаем флаг добавлены ли все контакты во все группы
    has_contacts_not_in_group = False

# получаем контакты, которые не в группе
    for i in range(len(group_list)):
        group = group_list[i]

        contacts_not_in_group = db.get_contacts_not_in_group(group)
        # если существуют контакты, которые не в группе, то мы берем 1й контакт и добавляем в эту группу
        if (len(contacts_not_in_group) > 0):
            quantity_contacts_in_group = db.get_contacts_in_group(group)
            app.contact_helper.contact_add_to_group(group, contacts_not_in_group[0].id)
            # делаем проверку что мы до бавили этот контакт в эту группу
            new_quantity_contacts_in_group = db.get_contacts_in_group(group)
            assert len(quantity_contacts_in_group) + 1 == len(new_quantity_contacts_in_group)
            has_contacts_not_in_group = True
            break

# если все контакты во всех группах, то создаём новый котакт и связываем его с группой
    if has_contacts_not_in_group is not True:
        # создаём нов контакт
        new_contact = Contact(firstname="el_contacto")
        app.contact_helper.create_contact(new_contact)
        app.contact_helper.save_contact()
        # берём первую группу в которую будем добавлять контакт
        group = group_list[0]
        # создаём списки для сравнения количества контактов в группе
        quantity_contacts_in_group = db.get_contacts_in_group(group)
        len_quantity_contacts_in_group = len(quantity_contacts_in_group)
        # берём последний созданный котакт и связываем с группой
        new_contact_from_db = db.get_contact_list()[-1]
        app.contact_helper.contact_add_to_group(group, new_contact_from_db.id)
        # сравниваем длину контактов
        new_quantity_contacts_in_group = len(db.get_contacts_in_group(group))
        assert len_quantity_contacts_in_group + 1 == new_quantity_contacts_in_group
