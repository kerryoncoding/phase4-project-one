from config import app

from models import User, Squad



class User(Resource):
  def post(self):
    form_json = request.get_json()
    new_user = User(
      name=form_json['name'],
      email=form_json['email']
    )
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id

    response = make_response{
      new_user.to_dict(),
      201
    }
    return response
api.add_resource(Users, '/users')





# app = Flask(__name__)

# @app.route('/')
# def index():
    # body = {'message': 'Welcome to the pet directory!'}
    # return make_response(body, 200)def index():

# @app.route('/<string:username>')
# def pet_by_id(id):
#     pet = Pet.query.filter(Pet.id == id).first()

#     if pet:
#         body = pet.to_dict()
#         status = 200
#     else:
#         body = {'message': f'Pet {id} not found.'}
#         status = 404

#     return make_response(body, status)


# @app.route('/squads')
# def squads():

#     squads = []
#     for squad in Squad.query.all():
#         squad_dict = {
#             "name": squad.name,
#             "description": squad.description,
#         }
#         squads.append(squad_dict)

#     response = make_response(
#         jsonify(squads),
#         200
#     )

#     return response


if __name__ == "__main__":
  app.run(port=5555, debug=True)
