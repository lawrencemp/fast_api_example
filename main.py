from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from Utilities.laptop_db_reader import Laptop
from Utilities.segment_db_reader import Price

app = FastAPI()

@app.get("/top_laptops/price_segments")
async def get_price_segments():
    prices = Price.get_price_segments()
    if prices is None:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Внутренняя ошибка сервера"}
        )
    return prices


@app.get("/top_laptops/{price_segment_id}")
async def get_top_laptop(price_segment_id: int):
      price_segment = Price.get_price_segment(price_segment_id)
      if price_segment is None:
          return JSONResponse(
              status_code=status.HTTP_404_NOT_FOUND,
              content={"message": "Не определен сегмент цен с таким номером"}
          )
      laptop = Laptop(price_segment_id)
      return laptop



