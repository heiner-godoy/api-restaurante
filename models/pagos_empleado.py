from sqlalchemy import Column, ForeignKey, Integer, Boolean, DateTime, String, Numeric, Text
from datetime import timezone, datetime
from sqlalchemy.orm import relationship
from database import Base


class PagoEmpleado(Base):
    __tablename__ = "pago_empleado"
    
    id_pago = Column(Integer, primary_key= True, unique=True)
    id_empleado = Column(Integer, ForeignKey("empleados.id_empleado"), nullable=False)
    monto = Column(Numeric, nullable=False)
    fecha = Column(DateTime, nullable=False)
    nota = Column(Text, nullable=True)
    creado_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    id_empleado = relationship("Empleados", back_populates="pago_empleado")