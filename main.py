from typing import Any

from fastapi import FastAPI
import typing



app = FastAPI()

@app.get('/api1')
async def root() -> typing.Dict[str, str]:
    return {'message': 'hello, world!'}

@app.get('/num')
async def root() -> int:
    return 12

@app.get('/api2')
async def root() -> typing.Dict[str, float]:
    return {'Message': 2.1}

@app.get('/api3')
async def root() -> typing.List[Any]:
    return [1, 1, '1', '1']

@app.get('/api4')
async def root() -> typing.Tuple:
    numbers = [i for i in range(1, 101)]
    return tuple(numbers)