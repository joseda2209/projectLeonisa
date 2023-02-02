import datetime
from pydantic import BaseModel,Field

class ReportByDateSchema(BaseModel):
    start_date_str: str = Field(
        default='2000-01-01',
        title='Start Date',
        description='Date to start report',
        regex=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
    final_date_str: str = Field(
        default='2030-01-01',
        title='Final Date',
        description='Date to end report',
        regex=r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    )
