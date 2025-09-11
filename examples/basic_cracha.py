from imprint import Model
import os

example_photo = os.path.join(os.getcwd(), "examples/assets/photo.png")

def basic_cracha():
    cracha = Model.new(
        name="Modelo-Cracha-Basico"
    )
    page_front = cracha.new_page(name="front")
    # Criando a pagina da frente do modelo
    page_front.set_size(500, 500)
    img_path = os.path.join(os.getcwd(), "examples/assets/cracha.png")
    page_front.set_background(img_path)
    # Criando campo de texto para nome
    field_full_name = page_front.add_field(name="Full Name", component="text")
    field_full_name.set_position((520, 320))
    # Criando campo de texto para job
    field_job = page_front.add_field(name="Cargo", component="text")
    field_job.set_position((510, 400))
    # Criando campo de texto para nivel de acesso
    field_acess = page_front.add_field(name="Role", component="text")
    field_acess.set_position((610, 480))
    # Criando campo de imagem para foto
    field_photo = page_front.add_field(name="Photo", component="img")
    field_photo.set_position((35, 245))
    field_photo.set_dimesion((360, 360))
    return cracha