# signup/login 
# create note
# summarize note
# save note
# get notes

from fastapi import FastAPI
from backend.routes.register import login
from backend.routes.notes import note


app=FastAPI()


app.include_router(login)

app.include_router(note)



