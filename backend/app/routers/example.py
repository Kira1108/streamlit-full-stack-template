from fastapi import APIRouter
import logging
from app.schemas import IntegerInput,IntegerOutput


log = logging.getLogger('uvicorn')

router = APIRouter(
    prefix="/example",
    tags=["example"],
    responses={404: {"description": "Not found"}},
)

@router.post("/example", response_model=IntegerOutput)
def example(value:IntegerInput):
    return IntegerOutput(value = value.value)