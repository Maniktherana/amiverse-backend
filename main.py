import logging
from typing import Union

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from google.protobuf.json_format import MessageToJson

from controllers import rpc_calls
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Date(BaseModel):
    date: dict

logger = logging.getLogger()

@app.get("/")
async def root():
    return {"message": "AmiVerse API running"}


@app.get("/classSchedule")
async def get_class_schedule(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_class_schedule(username, password)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")

@app.get("/userProfile")
async def get_user_profile(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_user_profile(username, password)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")

@app.get("/currentCourses")
async def get_current_course(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_current_course(username, password)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")

@app.get("/attendance")
async def get_attendance(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_attendance(username, password)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")

@app.get("/examSchedule")
async def get_exam_schedule(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_exam_schedule(username, password)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")

@app.get("/wifiInfo")
async def get_wifi_info(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_wifi_info(username, password)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")



