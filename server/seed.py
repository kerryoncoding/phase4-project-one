from config import app, db, User, Squad

if __name__ == "__main__":
  with app.app_context():
    users = []
    squads = []

    users.append(User(username = "Alice", email = "alice@gmail.com" ))
    users.append(User(username = "Brian", email = "brian@gmail.com" ))
    users.append(User(username = "Justin", email = "justin@gmail.com" ))
    users.append(User(username = "Dana", email = "Dana@gmail.com" ))

    squads.append(Squad(name = "PodSquad", podcast = "We can do hard things" ))
    squads.append(Squad(name = "Dax Chats", podcast = "Armchair Expert" ))
    squads.append(Squad(name = "Ask to Laugh", podcast = "Don't Ask Tig" ))
    squads.append(Squad(name = "Boys club", podcast = "Smartless" ))

    db.session.add_all(users)
    db.session.add_all(squads)
    db.session.commit()
