import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, DateTime, String, Numeric, Date
from datetime import timezone, datetime
from sqlalchemy.orm import relationship
from database import Base

class Metodo(str, enum.Enum):
    transferencia = "Transferencia"
    efectivo = "Efectivo"
    
class Ventas(Base):
    __tablename__ = "ventas"
    
    id_venta = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"), nullable=False, unique=True)
    fecha = Column(DateTime, nullable=False)
    metodo_pago = Column(Enum(Metodo), nullable=False)
    monto_recibido = Column(Numeric, nullable=False)
    cambio = Column(Numeric, nullable=False)
    total = Column(Numeric, nullable=False)
    creado_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    pedido = relationship("Pedidos", back_populates="venta")