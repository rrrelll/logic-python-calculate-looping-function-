from fastapi import APIRouter

router = APIRouter()


@router.get("/mahasiswa")
def cetak_mahasiswa(nama: str, umur: int):
    return {"pesan": f"{nama} adalah mahasiswa TI Unpam berusia {umur} tahun."}
