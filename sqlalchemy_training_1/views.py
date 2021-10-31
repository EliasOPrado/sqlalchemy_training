from models import User
from config import Base, engine, session



user = User(name='John Snow', password='johnspassword')
session.add(user)
session.commit()
# query = session.query(User).all()
print(user) 