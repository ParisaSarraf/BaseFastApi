from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from auth import authentication
from exceptions import EmailNotValid
from router import user, access

# =======================================================
# object of FastAPI
app = FastAPI()
#  1qazXSW@


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add object files into main page
app.include_router(user.router)
app.include_router(access.router)
app.include_router(authentication.router)


# =======================================================
# create table in database
# models.my_base.metadata.create_all(my_engine, checkfirst=False)
# =======================================================
# home page in tag home
@app.get('/', tags=['home'])
async def home_page():
    return {'message': 'home page'}


# custom error request
@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


# run in network
# uvicorn tut_main_19:app --host 0.0.0.0 --port 8000 --reload

# run in local
# uvicorn tut_main_19:app --reload

# debug mode
# --reload
