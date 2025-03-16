from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# تكوين CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # السماح لجميع النطاقات، يمكنك تحديد نطاقات معينة
    allow_credentials=True,
    allow_methods=["*"],  # السماح بجميع الطرق (GET, POST, PUT, DELETE, إلخ.)
    allow_headers=["*"],  # السماح بجميع الرؤوس
)

@app.get("/data")
async def get_data():
    return {"message": "Hello from FastAPI with CORS!"}

# تشغيل التطبيق
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
