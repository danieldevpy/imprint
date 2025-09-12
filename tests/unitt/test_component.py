from imprint import Model
from imprint.components import Text, Img

def test_component_text():
    # Criando o Modelo de Cracha Basico
    component =(
        Model.new("new model")
        .new_page("frente")
        .add_component(name="name", component="text")
    )
    assert isinstance(component, Text)
    assert component.get_color() == (0, 0, 0)
    assert component.get_size() == 12
    assert component.get_position() == (0, 0)

def test_component_img():
    # Criando o Modelo de Cracha Basico
    component =(
        Model.new("new model")
        .new_page("frente")
        .add_component(name="img", component="img")
    )
    assert isinstance(component, Img)
    assert component.get_position() == (0, 0)
    assert component.get_dimension() == (100, 100)