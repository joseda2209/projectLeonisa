from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.purchase import PurchaseService, PurchaseSchema

purchase_router = APIRouter()

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@purchase_router.post('/purchase')
def make_purchase(
    purchase: PurchaseSchema = Body(...),
    db: Session = Depends(get_db)
):
    result = PurchaseService(db).make_purchase(purchase)
    return JSONResponse(
        status_code=200, 
        content={
            'message':'se ha registrado la compra correctamente',
            'model':jsonable_encoder(result)
            }
    )