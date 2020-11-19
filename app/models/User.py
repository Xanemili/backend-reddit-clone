from . import db
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, LargeBinary
from werkzeug.security import generate_password_hash, check_password_hash

#dont forget user mixin
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(200), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
