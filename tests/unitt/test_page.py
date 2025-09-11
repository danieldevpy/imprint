from imprint import Model, Page

def test_page():
    # Criando o Modelo de Cracha Basico
    page = Model.new("new model").new_page("frente")
    assert isinstance(page, Page)
    assert page.options.name == "frente"
    assert page.options.width == 0
    assert page.options.height == 0
    assert page.options.background == None
    assert page.options.background_color == (0, 0, 0, 0)
    assert len(page.fields) == 0