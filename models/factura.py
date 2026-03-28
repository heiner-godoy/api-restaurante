from sqlalchemy import Column, Integer, DateTime, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from datetime import timezone, datetime
from database import Base

class Factura(Base):
    __tablename__ = "facturas"
    
    id_factura = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String(50), unique=True, nullable=False)  # folio o consecutivo
    id_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"), nullable=False)
    id_venta = Column(Integer, ForeignKey("ventas.id_venta"), nullable=False)   
    
    # Datos propios de la factura
    fecha_emision = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    cliente_nombre = Column(String(100), nullable=False)
    cliente_direccion = Column(String(255), nullable=True)
    cliente_telefono = Column(String(50), nullable=True)
    
    metodo_pago = Column(String(50), nullable=False)
    total = Column(Numeric, nullable=False)
    
    # Relaciones
    pedido = relationship("Pedidos", back_populates="factura")
    venta = relationship("Ventas", back_populates="factura")
    empacador = relationship("Empleados", back_populates="facturas_empacadas")