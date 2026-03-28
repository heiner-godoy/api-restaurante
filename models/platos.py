from sqlalchemy import Column, Integer, Boolean, DateTime, String, Numeric, Text
from datetime import timezone, datetime
from sqlalchemy.orm import relationship
from database import Base


class Platos(Base):
    __tablename__ = "platos"
    
    id_plato = Column(Integer, autoincrement=True, primary_key=True)
    
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric, nullable=False)
    categoria = Column(String(50), nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    creado_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    detalles = relationship("PedidoDetalles", back_populates="platos")

