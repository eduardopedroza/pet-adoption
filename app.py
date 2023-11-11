from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SECRET!"

@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():

        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo.data,
            age = form.age.data,
            notes = form.notes.data
        )

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    return render_template('add_pet_form.html')
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_detail(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    
    return render_template('pet_page.html', form=form, pet=pet)
    


