from Utilities.db_connect import Session
from Utilities.db_connect import TopLaptop
from Utilities.db_connect import PriceSegment
import json


class Laptop():
    def __init__(self, price_id):
        with Session() as db:
            laptop_db = db.query(TopLaptop).filter(TopLaptop.price_segment_id == price_id).first()
            price_segment_db = db.query(PriceSegment).filter(PriceSegment.id == price_id).first()
            self.link: str = laptop_db.link
            self.price_segment: str = f'{price_segment_db.bottom_line} - {price_segment_db.top_line}'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
