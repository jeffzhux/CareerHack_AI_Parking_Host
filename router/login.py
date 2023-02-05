
from fastapi import APIRouter
from model.security_guard import Security_Guard
from controller import security_guard
router = APIRouter()

@router.post("/login", tags=['登入'])
async def login(sg_info: Security_Guard) -> dict:
    return await security_guard.login(sg_info)

@router.get("/login/get_security_guard", tags=['警衛清單'])
async def get_security_guard() -> dict:
    return await security_guard.get_security_guard()



