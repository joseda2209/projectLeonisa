from fastapi import APIRouter, Depends, Path, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.product import ProductService
from schemas.product import ProductSchema

product_router = APIRouter()

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@product_router.get('/product')
def get_products(db: Session = Depends(get_db)) :
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.get('/product/{id_product}')
def get_one_product(
    id_product: str = Path(
        ...,
        title = 'idProducto',
        description='identificador unico del producto'
    ),
    db: Session = Depends(get_db)
):
    result = ProductService(db).get_one_product(id_product)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@product_router.post('/product')
def create_product(
    product: ProductSchema = Body(...),
    db: Session = Depends(get_db)
):
    result = ProductService(db).create_product(product)
    return JSONResponse(
        status_code=200, 
        content={
            'message':'se ha registrado correctamente',
            'model': jsonable_encoder(result)
            }
        )