from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from models.factura import TipoImpresion, EstadoFactura

class CreateFactura(BaseModel):
    id_venta       : int           = Field(..., description="ID de la venta")
    numero         : str           = Field(..., max_length=20, description="Número de factura")
    tipo_impresion : TipoImpresion = Field(..., description="empacador | cliente")

class ResponseFactura(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_factura     : int
    id_venta       : int
    numero         : str
    tipo_impresion : TipoImpresion
    estado         : EstadoFactura
    creado_en      : Optional[datetime]

class UpdateFactura(BaseModel):
    estado : Optional[EstadoFactura] = None