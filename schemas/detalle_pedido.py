from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from decimal import Decimal
from models.detalle_pedido import TipoSopa

class CreatePedidoDetalle(BaseModel):
    id_pedido : int            = Field(..., description="ID del pedido")
    id_plato  : int            = Field(..., description="ID del plato")
    tipo_sopa : Optional[TipoSopa] = None
    cantidad  : int            = Field(..., gt=0)
    notas     : Optional[str]  = None
    subtotal  : Decimal        = Field(..., description="Subtotal del detalle")

class ResponsePedidoDetalle(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_detalle : int
    id_pedido  : int
    id_plato   : int
    tipo_sopa  : Optional[TipoSopa]
    cantidad   : int
    notas      : Optional[str]
    subtotal   : Decimal

class UpdatePedidoDetalle(BaseModel):
    tipo_sopa : Optional[TipoSopa] = None
    cantidad  : Optional[int]      = None
    notas     : Optional[str]      = None
    subtotal  : Optional[Decimal]  = None