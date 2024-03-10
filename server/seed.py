
from app import app
from models import db, Squad


with app.app_context():
  #  Delete all rows in tables
  squads = []

  #  add squads
  # squads.append(Squad(name='Sunday Sitdown', image='https://image.simplecastcdn.com/images/4bf8292b-a5be-4d3a-a88c-328f0f42e38f/79d98736-2db7-473a-b591-191163d66a87/3000x3000/ss-jonbatiste-episodicartwork.jpg?aid=rss_feed', description='Conversations with Willie Geist and speical guests'))
  # squads.append(Squad(name='Armchair Expert', image='https://i.iheart.com/v3/url/aHR0cHM6Ly9tZWdhcGhvbmUuaW1naXgubmV0L3BvZGNhc3RzLzFmNmJmY2VjLTIyNzQtMTFlZS04ZWQxLTU3NTcxOTQ0ZDgyZi9pbWFnZS9Bcm1jaGFpcl9FeHBlcnRfLV9BX1Nwb3RpZnlfUG9kY2FzdC5qcGc_aXhsaWI9cmFpbHMtNC4zLjEmbWF4LXc9MzAwMCZtYXgtaD0zMDAwJmZpdD1jcm9wJmF1dG89Zm9ybWF0LGNvbXByZXNz', description='Dax Shepard dishing adivce'))
  # squads.append(Squad(name='Don\'t Ask Tig', image='https://img.apmcdn.org/62790abdbd1ccfe17022faf1b235df1100d97628/normal/56a01d-20200622-don-t-ask-tig-podcast-tile.jpg', description='The adivce you shouldn\'t have asked for'))
  # squads.append(Squad(name='We Can Do Hard Things', image='https://m.media-amazon.com/images/M/MV5BNjhiYTg1NDAtMTZmOS00YzA0LWI2YjMtMjQ4NTVlMWI3OTUwXkEyXkFqcGdeQXVyMTU3MzMwNQ@@._V1_.jpg', description='Tune in for Inspriation when you need it'))


  squads.append(Squad(name='Sunday Sitdown', image='https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png', description='Conversations with Willie Geist and speical guests'))
  squads.append(Squad(name='Armchair Expert', image='https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png', description='Dax Shepard dishing adivce'))
  squads.append(Squad(name='Don\'t Ask Tig', image='https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png', description='The adivce you shouldn\'t have asked for'))
  squads.append(Squad(name='We Can Do Hard Things', image='https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png', description='Tune in for Inspriation when you need it'))

  db.session.add_all(squads)
  db.session.commit()

