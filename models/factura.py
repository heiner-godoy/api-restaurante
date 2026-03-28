# models/factura.py
from sqlalchemy import Column, Integer, DateTime, String, Numeric, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import timezone, datetime
import enum
from database import Base

class TipoImpresion(str, enum.Enum):
    empacador = "empacador"
    cliente   = "cliente"

class EstadoFactura(str, enum.Enum):
    pendiente  = "pendiente"
    entregada  = "entregada"
    cancelada  = "cancelada"

class Factura(Base):
    __tablename__ = "facturas"

    id_factura     = Column(Integer, primary_key=True, autoincrement=True)
    id_venta       = Column(Integer, ForeignKey("ventas.id_venta"), nullable=False)
    numero         = Column(String(20), unique=True, nullable=False)
    tipo_impresion = Column(Enum(TipoImpresion), nullable=False)
    estado         = Column(Enum(EstadoFactura), default=EstadoFactura.pendiente)
    creado_en      = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    venta = relationship("Ventas", back_populates="facturas")