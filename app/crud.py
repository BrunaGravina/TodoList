from app.models import Task
from sqlalchemy.orm import Session


def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, title: str):
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task_status(db: Session, task_id: int, is_complete: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.is_complete = is_complete
    db.commit()
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(task)
    db.commit()
