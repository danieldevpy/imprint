from imprint import Model
import os

def create_basic_badge():
    background_path = os.path.join(os.getcwd(), "examples/assets/badge.png")

    model = Model.new(name="Basic-Badge")

    front_page = model.new_page(name="front")
    front_page.set_background(background_path)

    full_name_field = front_page.add_component(name="Full Name", component="text", form_key="name")
    full_name_field.set_position((520, 320))
    full_name_field.set_size(24)

    job_field = front_page.add_component(name="Job", component="text", form_key="job")
    job_field.set_position((510, 400))
    job_field.set_size(24)

    role_field = front_page.add_component(name="Role", component="text", form_key="role")
    role_field.set_position((610, 480))
    role_field.set_size(24)

    photo_field = front_page.add_component(name="Photo", component="img", form_key="photo")
    photo_field.set_position((35, 245))
    photo_field.set_dimension((360, 360))

    return model