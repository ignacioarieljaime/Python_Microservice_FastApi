from fastapi import APIRouter , Form, Depends, File, UploadFile
from util.custom_routes import FileStreamRoute
from util.auth_session import get_current_user

router = APIRouter()
router.route_class = FileStreamRoute

@router.post("/files/")
async def create_file(file: bytes = File(...), params: str = Form (...), user: str = Depends(get_current_user)):
    
    return {"file_size": len(file)}


@router.post("/files/upload")
async def create_file_2(file: UploadFile = File(...) , user: str = Depends(get_current_user)):
    print(file.content_type)
    fs = await file.read()
    return {"file_size": len(fs)}
    
