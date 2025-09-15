from imprint import Model
import os

def create_basic_badge():
    # Getting background image path
    background_path = os.path.join(os.getcwd(), "examples/assets/badge.jpeg")
    
    # Creating basic model
    model = Model.new(name="Basic-Badge")

    # Creating front page
    front_page = model.new_page(name="front")\
        .set_background(background_path)

    # Adding text field: name
    front_page.add_component(name="Full Name", component="text", form_key="name")\
        .set_position((520, 320))\
        .set_size(24)  # defining component properties

    # Adding text field: job
    front_page.add_component(name="Job", component="text", form_key="job")\
        .set_position((510, 400))\
        .set_size(24)  # defining component properties

    # Adding text field: role
    front_page.add_component(name="Role", component="text", form_key="role")\
        .set_position((610, 480))\
        .set_size(24)  # defining component properties

    # Adding image field: photo
    front_page.add_component(name="Photo", component="img", form_key="photo")\
        .set_position((35, 245))\
        .set_dimension((360, 360))  # defining component properties

    return model