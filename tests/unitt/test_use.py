
from examples.basic_cracha import create_basic_badge
import os



def tests_use():
    model = create_basic_badge()
    model.build_img
    # model = create_basic_badge()
    # model.export("data.json")
    # # Construir e renderizar (com o engine Pillow por padrão)
    # resultado = model.build(dados_formulario_list).render()

    # # Visualizar no visualizador padrão do sistema
    # resultado.save("teste.pdf")

photo_path = os.path.join(os.getcwd(), "examples/assets/photo.jpeg")

dados_formulario_list = [
    {
        "name": "Daniel Fernandes Pereira",
        "job": "Desenvolvedor de Software",
        "role": "Administrador",
        "photo": photo_path,
    },
    {
        "name": "Ana Souza Lima",
        "job": "Designer Gráfico",
        "role": "Usuário",
        "photo": photo_path,
    },
    {
        "name": "Carlos Eduardo Silva",
        "job": "Analista de Dados",
        "role": "Moderador",
        "photo": photo_path,
    },
    {
        "name": "Mariana Costa",
        "job": "Gerente de Projetos",
        "role": "Administrador",
        "photo": photo_path,
    },
]
