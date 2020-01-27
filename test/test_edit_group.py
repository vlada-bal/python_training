from model.group import Group

def test_edit_group(app):
    group = Group(name="u koshki", header="tolstie", footer="nojki")
    app.group_helper.edit_group(group)
