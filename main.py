import logging
from datetime import datetime

from fastapi import FastAPI, Request, Response
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
logger.setLevel(logging.INFO)

# Create a custom logging format
log_format = '%(asctime)s - %(levelname)s: %(message)s'

# Create a StreamHandler and set the log format
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(log_format))

# Add the StreamHandler to the logger
logger.addHandler(stream_handler)

@app.get("/")
async def root():
    request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"Request at {request_time}: AmiVerse API running")
    return {"message": "AmiVerse API running"}

@app.middleware("http")
async def log_request(request: Request, call_next):
    request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"Request at {request_time}: {request.method} {request.url}")
    response = await call_next(request)
    return response

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

@app.get("/courses")
async def get_courses_by_sem(username, password, semester):
    print("Getting user profile", username, password, semester)
    res = await rpc_calls.get_courses(username, password, semester)
    json_data= MessageToJson(res)
    return Response(content=json_data, media_type="application/json")

@app.get("/semesters")
async def get_semesters(username, password):
    print("Getting user profile", username, password)
    res = await rpc_calls.get_semesters(username, password)
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



