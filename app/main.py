from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import get_tasks, create_task, update_task_status, delete_task
from app.db import SessionLocal, engine, Base
from app.schemas import TaskCreate, TaskUpdate
from app.auth import get_current_user
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@app.post("/tasks")
def add_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_task(db, task.title)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return update_task_status(db, task_id, task.is_complete)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return delete_task(db, task_id)
