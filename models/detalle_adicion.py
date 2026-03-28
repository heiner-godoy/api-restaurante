from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base

class DetalleAdiccion(Base):
    __tablename__ = "detalle_adiciones"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_detalle = Column(Integer, ForeignKey("pedido_detalles.id_detalle"), nullable=False)
    id_adiccion = Column(Integer, ForeignKey("adicciones.id_adiccion"), nullable=False)
    cantidad = Column(Numeric, nullable=False)
    
    detalle_pedido = relationship("PedidoDetalles", back_populates="detalle_adiciones")
    adiccion = relationship("Adicciones", back_populates="detalle_adiciones")