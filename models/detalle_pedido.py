import enum
from sqlalchemy import Column, Integer, ForeignKey, Text, Numeric, Enum
from sqlalchemy.orm import relationship
from database import Base


class TipoSopa(str, enum.Enum):
    carne    = "carne"
    gallina  = "gallina"
    pusandao = "pusandao"
    pata     = "pata"
    pescado  = "pescado"


class PedidoDetalles(Base):
    __tablename__ = "pedido_detalles"

    id_detalle = Column(Integer, primary_key=True, autoincrement=True)
    id_pedido  = Column(Integer, ForeignKey("pedidos.id_pedido"), nullable=False)
    id_plato   = Column(Integer, ForeignKey("platos.id_plato"), nullable=False)
    tipo_sopa  = Column(Enum(TipoSopa), nullable=True)
    cantidad   = Column(Integer, nullable=False, default=1)  # ← Integer no Numeric
    notas      = Column(Text, nullable=True)
    subtotal   = Column(Numeric(10, 2), nullable=False)

    pedido            = relationship("Pedidos", back_populates="detalles")
    plato             = relationship("Platos", back_populates="detalles")
    detalle_adiciones = relationship("DetalleAdiccion", back_populates="detalle_pedido")