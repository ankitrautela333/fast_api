from fastapi import APIRouter, Response, Body

router = APIRouter(prefix='/post2',
                   tags=['post2'])


@router.post("/asdf",tags=['12133'], description="if greatert than 10 than 34343",summary="check value")
async def aaaaa(response: Response, l=Body()):
    if int(l) > 10:
        response.status_code = 404
        return ("34343")
    else:
        response.status_code = 200
        return (l)
