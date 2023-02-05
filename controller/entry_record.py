
from model.database import pool
import sqlalchemy

async def get_entry_record_by_ER_PLID(PL_ID: str):
    cmd = sqlalchemy.text(
        "select * from parking.ENTRY_RECORD where PL_ID=:PL_ID"
    )
    with pool.connect() as db_conn:
        db_conn.excute(cmd, PL_ID=PL_ID)
    return {"msg":"PL_ID"}