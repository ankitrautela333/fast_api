import uvicorn
from fastapi import FastAPI, Body, Response, APIRouter

router = APIRouter(prefix='/post',
                   tags=['post_put'])


@router.post("/news/{nes_no}", response_description="this is it")
async def abcd(nes_no: int, rands=Body()):
    """
    retunr the value directly
    """
    print(nes_no)
    return (nes_no, rands)


@router.post("/last", tags=['12133'], description="if greatert than 10 than 34343", summary="check value")
async def abcd(response: Response, l=Body()):
    if int(l) > 10:
        response.status_code = 404
        return ("34343")
    else:
        response.status_code = 200
        return (l)


@router.put("/bn")
async def put_http(l=Body()):
    return (10, l)
