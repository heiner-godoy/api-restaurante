from sqlalchemy import Column, ForeignKey, Integer, DateTime, Numeric, Text
from datetime import timezone, datetime
from sqlalchemy.orm import relationship
from database import Base


class PagoEmpleado(Base):
    __tablename__ = "pagos_empleado"

    id_pago     = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, ForeignKey("empleados.id_empleado"), nullable=False)
    monto       = Column(Numeric(10, 2), nullable=False)
    fecha       = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    nota        = Column(Text, nullable=True)
    creado_en   = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    empleado = relationship("Empleados", back_populates="pagos")  # ← nombre correcto