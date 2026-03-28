import enum
from sqlalchemy import Column, ForeignKey, Integer, Boolean, DateTime, String, Numeric, Text, Enum
from datetime import timezone, datetime
from sqlalchemy.orm import relationship
from database import Base

class EstadoPedido(str, enum.Enum):
    pagado = "pagado"
    pendiente = "pendiente"
    
class TipoEntrega(str, enum.Enum):
    domicilio = "domicilio"
    recoge = "recoge"
    mesa = "mesa"


class Pedidos(Base):
    __tablename__ = "pedidos"
    
    id_pedido = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id_empleado = Column(Integer, ForeignKey("empleados.id_empleado"), nullable=False)
    tipo_entrega = Column(Enum(TipoEntrega), nullable=False)
    numero_mesa = Column(Integer, nullable=True)
    cliente_nombre = Column(String(50), nullable=True)
    cliente_telefono = Column(String(50), nullable=True)
    cliente_direccion = Column(Text, nullable=True)
    estado = Column(Enum(EstadoPedido), nullable=False)
    creado_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    empleado = relationship("Empleados", back_populates="pedidos")
    detalles = relationship("PedidoDetalles", back_populates="pedido")
    venta = relationship("Ventas", back_populates="pedido", uselist=False)
    factura = relationship("Factura", back_populates="pedido", uselist=False)  

