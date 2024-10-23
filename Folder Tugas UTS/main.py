from fastapi import FastAPI
from Tugas1.InputDataMhsw import router as InputDataMhsw_router
from Tugas2.aritmatika import router as aritmatika_router
from Tugas3.CekUmur import router as CekUmur_router


app = FastAPI(title="Muhammad Tafarel Akbar",description="231011400175")


# Menyambungkan Router

app.include_router(aritmatika_router)
app.include_router(InputDataMhsw_router)
app.include_router(CekUmur_router)


if __name__ == "___main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)