from multiprocessing import Process

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import user

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000", # 허용할 프론트앤드 도메인
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(user.router)

def run_server(port):
    uvicorn.run('main:app', port=port, reload=True)

if __name__ == '__main__':
    process1 = Process(target=run_server, args=(8000,))
    process1.start()

    process1.join()
