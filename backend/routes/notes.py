# notes.py

from fastapi import APIRouter, Depends,HTTPException
from backend.routes.register import get_current_user
from backend.db import get_connection
from pydantic import BaseModel
note = APIRouter()

class Notes(BaseModel):
    content:str

# class UpdateNotes(BaseModel):
#     notes_id:int
#     content:str

@note.get("/notes")
def get_notes(
    user_id: str = Depends(get_current_user)
):
    
    try:
        con=get_connection()
        cur=con.cursor(dictionary=True)
        cur.execute("select notes_id, notes from notes where user_id=%s",(int(user_id),))
        notes=cur.fetchall()
        
        
        return notes
    finally:
        cur.close()
        con.close()
    


        
        
        
@note.post("/notes")
def add_notes(note:Notes,user_id:str=Depends(get_current_user)):
    try:
        con=get_connection()
        cur=con.cursor(dictionary=True)
        cur.execute("insert into notes (notes,user_id) values(%s,%s)",(note.content,int(user_id)))
        con.commit()
        return {"message": "Note added successfully",
                "note":note.content
                }

    finally:
        cur.close()
        con.close()

@note.patch("/notes/{notes_id}")
def update_notes(notes_id:int,note:Notes,user_id:str=Depends(get_current_user)):
    try:
        con=get_connection()
        cur=con.cursor(dictionary=True)
        cur.execute("""
                    update notes
                    set notes=%s
                    where user_id=%s and notes_id=%s

""",(note.content,int(user_id),notes_id))
        
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Note not found"
                  )

        return {
            "message":"Note updated successfully",
            "content":note.content
        }

    finally:

        cur.close()
        con.close()


@note.delete("/notes/{notes_id}")
def delete_notes(notes_id:int,user_id:str=Depends(get_current_user)):
    try:
        con=get_connection()
        cur=con.cursor(dictionary=True)
        cur.execute("delete from notes where user_id=%s and notes_id=%s",(int(user_id),notes_id))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Note not found")
        return {"message": "Note deleted successfully"}
    finally:
        cur.close()
        con.close()