import enum
from sqlalchemy import Column, Enum, Integer
from sqlalchemy.orm import relationship
from database import Base

class TipoRol(str, enum.Enum):
    admin = "admin"
    cajera = "cajera"
    mesera = "mesera"

class Rol(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(Enum(TipoRol, name="tipo_rol"), nullable=False, unique=True)

    usuarios = relationship("Usuarios", back_populates="rol")
