from app import db
from app.models import User, Post

users = User.query.all()
users

u = User.query.get(1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

u = User.query.get(2)
u.posts.all()

for u in users:
    db.session.delete(u)