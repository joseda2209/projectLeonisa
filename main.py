from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field
from fastapi import FastAPI, Body, Query, Path
from config.database import Session, engine, Base
from models import product, purchase, purchase_detail
from middlewares.error_handler import ErrorHandler
from routers import product, purchase, reports

Base.metadata.create_all(engine)

app = FastAPI()
app.title = "projectLeonisa"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(product.product_router)
app.include_router(purchase.purchase_router)
app.include_router(reports.reports_router)
