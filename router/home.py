
from fastapi import APIRouter
from model.security_guard import Security_Guard
from controller import entry_record
router = APIRouter()

@router.get("/home/{PL_ID}", tags=['取得當前停車場入場車輛'])
async def get_entry_record_by_ER_PLID(PL_ID) -> dict:
    return await entry_record.get_entry_record_by_ER_PLID(PL_ID)

