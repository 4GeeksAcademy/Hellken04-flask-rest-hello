import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Date, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    ID: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str]=mapped_column(String(100), nullable=False)
    member_since: Mapped[datetime.date]=mapped_column(Date(),nullable=False)
    firstname: Mapped[str]=mapped_column(String(100), nullable=False)
    lastname: Mapped[str]=mapped_column(String(100), nullable=False)
    is_active: Mapped[bool]=mapped_column(Boolean,nullable=False, default=True)
    favorites: Mapped[list['FavoriteCharacters']]=relationship(back_populates='user')
    favorites_planets: Mapped[list['FavoritePlanets']]=relationship(back_populates='user')
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
           
        }

class Characters(db.Model):
    __tablename__='characters'
    ID: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String(120), nullable=False)
    height: Mapped[int]= mapped_column(Integer)
    weight: Mapped[int]= mapped_column(Integer)
    favorite_by: Mapped[list['FavoriteCharacters']]=relationship(back_populates='character')

class Planets (db.Model):
    __tablename__='planets'
    ID: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(100))
    population: Mapped[int]=mapped_column(Integer)
    favorite_by:Mapped[list['FavoritePlanets']]=relationship(back_populates='planet')

class FavoriteCharacters(db.Model):
    __tablename__='favorite_characters'
    ID: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped [int] = mapped_column(ForeignKey('user.ID'))
    user: Mapped['User']= relationship(back_populates='favorites')
    character_id: Mapped [int] = mapped_column(ForeignKey('characters.ID'))
    character: Mapped['Characters']= relationship(back_populates='favorite_by')

class FavoritePlanets (db.Model):
    __tablename__='favorite_planets'
    ID : Mapped[int]= mapped_column(primary_key=True)
    user_id: Mapped [int]=mapped_column(ForeignKey('user.ID'))
    user: Mapped['User']=relationship(back_populates='favorite_planets')
    planet_id:Mapped [int]= mapped_column(ForeignKey('planets.ID'))
    planet: Mapped['Planets']=relationship(back_populates='favorite_by')
    

    
