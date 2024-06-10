from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random as rand

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random", methods = ["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = rand.choice(all_cafes)
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })
    return jsonify(cafes={column.name: getattr(random_cafe, column.name) for column in random_cafe.__table__.columns})

# show all data
@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    #This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(cafes=[{column.name: getattr(cafe, column.name) for column in cafe.__table__.columns} for cafe in all_cafes])

# search by loc
@app.route("/search")
def get_search_cafes():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location.like(f"%{query_location}%")).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    #This uses a List Comprehension but you could also split it into 3 lines.
    if all_cafes:
        return jsonify(cafes=[{column.name: getattr(cafe, column.name) for column in cafe.__table__.columns} for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# get single id
@app.route("/cafe/<int:id>")
def get_cafe(id):
    cafe = db.get_or_404(Cafe, id)
    return jsonify(cafes={column.name: getattr(cafe, column.name) for column in cafe.__table__.columns})

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    form_dict = request.form.to_dict()
    for key, value in form_dict.items():
        if value == "true":
            form_dict[key] = True
        elif value == "false":
            form_dict[key] = False
    db.session.add(Cafe(**form_dict))
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods = ["PATCH"])
def update_cafe_price(id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, id)
    if cafe: 
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
# HTTP DELETE - Delete Record

if __name__ == '__main__':
    app.run(debug=True)
