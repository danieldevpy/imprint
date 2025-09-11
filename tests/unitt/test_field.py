from imprint import Model, Field, Text, Img

def test_field_text():
    # Criando o Modelo de Cracha Basico
    field =(
        Model.new("new model")
        .new_page("frente")
        .add_field("name", "text")
    )
    assert isinstance(field, Field)
    assert isinstance(field.component, Text)
    assert field.name == "name"
    assert field.component.color == (0, 0, 0)
    assert field.component.size == 24
    assert field.component.position == (0, 0)


def test_field_img():
    # Criando o Modelo de Cracha Basico
    field =(
        Model.new("new model")
        .new_page("frente")
        .add_field("img", "img")
    )
    assert isinstance(field, Field)
    assert isinstance(field.component, Img)
    assert field.name == "img"
    assert field.component.position == (0, 0)
    assert field.component.dimension == (100, 100)