from imprint import Model

def test_model():
    # Criando o Modelo de Cracha Basico
    model = Model.new("new model")
    assert isinstance(model, Model)
    assert model.name == "new model"
    assert len(model.pages) == 0