from sqlalchemy import Column, DateTime, String, Boolean, Numeric, Integer
from sqlalchemy.orm import relationship
from datetime import timezone, datetime
from database import Base


class Adicciones(Base):
    __tablename__ = "adicciones"
    id_adiccion = Column(Integer ,primary_key=True, autoincrement= True, unique=True)
    
    nombre = Column(String(50), nullable=False, unique= True)
    precio = Column(Numeric, nullable=False)
    activo = Column(Boolean, default=True)
    creado_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
