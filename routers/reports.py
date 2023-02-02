from typing import Optional
from fastapi import APIRouter, Depends, Query
from config.database import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.reports import ReportByDateSchema
from services.reports import ReportsService


reports_router = APIRouter()

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@reports_router.get('/purchasesByDate')
def get_report_purchases_by_date(
    start_date_str: Optional[str] = Query(
        default='2000-01-01',
        title='Start Date',
        description='Date to start report',
        regex=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
        ),
    final_date_str: str = Query(
        default='2030-01-01',
        title='Final Date',
        description='Date to end report',
        regex=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    ),
    db: Session = Depends(get_db)
):
    result = ReportsService(db).get_purchase_report_by_date(start_date_str, final_date_str)
    return JSONResponse(
        status_code=200, 
        content={
            'message':f'el reporte se genero en la ubicacion: {result}',
            }
    )