from Utilities.db_connect import PriceSegment
from Utilities.db_connect import Session


class Price:
    @staticmethod
    def get_price_segment(price_segment_id: int):
        with Session() as db:
            try:
                price = db.query(PriceSegment).filter(PriceSegment.id == price_segment_id).first()
                return price
            except Exception:
                return None

    @staticmethod
    def get_price_segments():
        with Session() as db:
            prices = db.query(PriceSegment).all()
            return prices
