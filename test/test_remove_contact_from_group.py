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

    # делаем флаг добавлен ли хоть один контакт в группу
    has_any_contacts_in_groups = False

    # создаем цикл в котором получаем список контактов для каждой группы
    for group in db.get_group_list():
        contact_list = db.get_contacts_in_group(group)
        # если в группе есть хоть один контакт, удаяем его из группы
        if (len(contact_list) > 0):
            has_any_contacts_in_groups = True
            contact_list_count = len(contact_list)
            contact_to_delete = contact_list[0]
            app.contact_helper.remove_contact_from_group(group, contact_to_delete.id)
            new_contact_list_count = len(db.get_contacts_in_group(group))
            assert contact_list_count - 1 == new_contact_list_count
            break

    first_group = db.get_group_list()[0]
    # кейс когда контакт с группой не связан
    if has_any_contacts_in_groups is not True:
        app.contact_helper.contact_add_to_group(first_group, first_group.id)
        contact_list = db.get_contacts_in_group(first_group, first_group.id)
        app.contact_helper.remove_contact_from_group(first_group, first_group.id)
        new_contact_list_count = db.get_contacts_in_group(first_group, first_group.id)
        # проверяем что удалилось
        assert len(contact_list) - 1 == len(new_contact_list_count)