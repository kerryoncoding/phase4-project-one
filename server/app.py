from config import app
# from distutils.log import debug
from flask_cors import CORS
from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import User, Squad, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)


@app.route('/api/squads', methods=['GET', 'POST'])
def squads():
  if request.method == 'GET':
    squads = Squad.query.order_by('created_at').all()

    response = make_response(
        jsonify([squad.to_dict() for squad in squads]),
        200,
    )
  
  elif request.method == 'POST':
      data = request.get_json()
      squad = Squad(
          name=data['name'],
          image=data['image'],
          description=data['description']
      )

      db.session.add(squad)
      db.session.commit()

      response = make_response(
          jsonify(squad.to_dict()),
          201,
      )

  return response


if __name__ == "__main__":
  app.run(port=5555, debug=True)
