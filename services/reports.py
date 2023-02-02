import os,csv
from datetime import datetime, timedelta
from typing import Any
from sqlalchemy.orm import Session
from services.purchase import PurchaseService


class ReportsService():
    HEADER_BY_DATE = ["DATE", "PURCHASE VALUE"]
    FORMAT_DATE = '%Y-%m-%d'
    REPORTS_PATH = r'D:\generate\reports'

    def __init__(self, db: Session) -> None:
        self.db = db


    def get_purchase_report_by_date(self, start_date_str: str, final_date_str: str):
        start_date = datetime.strptime(start_date_str, self.FORMAT_DATE)
        final_date = datetime.strptime(final_date_str, self.FORMAT_DATE)
        final_date += timedelta(days=1)
        print(start_date)
        print(final_date)
        purchases_by_date = PurchaseService(self.db).get_purchases_by_date(start_date, final_date)
        return self.generate_file(start_date_str, final_date_str, purchases_by_date)

    def generate_file(self, start_date_str: str, final_date_str: str, data: Any):
        file_name = f"Purchases_By_Date_{start_date_str}_{final_date_str}.csv"
        with open(os.path.join(self.REPORTS_PATH, file_name),"w") as report:
            csvwriter = csv.writer(report, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(['DATE', 'PURCHASE VALUE'])
            [csvwriter.writerow([datetime.strftime(purchase[0], self.FORMAT_DATE), purchase[1]]) for purchase in data]
        return os.path.join(self.REPORTS_PATH, file_name)
