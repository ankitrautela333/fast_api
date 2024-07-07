import uvicorn
from fastapi import FastAPI, Body, Response

from POST_PUT_OP import post_put, post_2

app = FastAPI()
app.include_router(post_put.router)
app.include_router(post_2.router)


Books = [
    {"title": "Title One", "author": "Author One", "category": "Category One"},
    {"title": "Title Two", "author": "Author Two", "category": "Category Two"},
    {"title": "Title Three", "author": "Author Three", "category": "Category Three"},
    {"title": "Title Four", "author": "Author Four", "category": "Category Four"},
    {"title": "Title Five", "author": "Author Five", "category": "Category Five"}
]


@app.get("/books/1")
async def read_all_books():
    return {"data": "sdc"}


@app.get("/books/{book_no}")
async def read_all_books(book_no):
    return {"data": book_no}


@app.get("/de",tags=["11","w"])
async def main():
    return ({"Detail": "Main News"})


@app.post("/news/{nes_no}",tags=["11"],response_description="this is it")
async def abcd(nes_no: int, rands=Body()):
    """
    retunr the value directly
    """
    print(nes_no)
    return (nes_no, rands)


@app.post("/last", description="if greatert than 10 than 34343",summary="check value")
async def abcd(response: Response, l=Body()):
    if int(l) > 10:
        response.status_code = 404
        return ("34343")
    else:
        response.status_code = 200
        return (l)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8000, reload=True)
