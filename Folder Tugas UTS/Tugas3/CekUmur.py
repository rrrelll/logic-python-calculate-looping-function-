from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List

router = APIRouter()

#Nama Bulan
nama_bulan = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]


class UmurRequest(BaseModel):
    bulan_lahir: int
    tahun_lahir: int
    bulan_mulai: int
    tahun_mulai: int
    bulan_akhir: int
    tahun_akhir: int
    bulan_yang_dipilih: List[int]  

# Fungsi For Loop
@router.post("/hitung-umur-for")
def hitung_umur_for(req: UmurRequest) -> List[Dict[str, str]]:
    hasil = []
    tahun_sekarang = req.tahun_mulai
    umur_tahun = req.tahun_mulai - req.tahun_lahir
    umur_bulan = req.bulan_mulai - req.bulan_lahir

    # untuk mengatasi bulan negaif
    if umur_bulan < 0:
        umur_tahun -= 1
        umur_bulan += 12

    
    for tahun in range(req.tahun_mulai, req.tahun_akhir + 1):
       
        if tahun == req.tahun_mulai:
            bulan_awal = req.bulan_mulai
        else:
            bulan_awal = 1
        
        if tahun == req.tahun_akhir:
            bulan_akhir = req.bulan_akhir
        else:
            bulan_akhir = 12

        # Loop untuk setiap bulan dalam tahun
        for bulan in range(bulan_awal, bulan_akhir + 1):
            if bulan in req.bulan_yang_dipilih:
                hasil.append({
                    "pada": f"{nama_bulan[bulan - 1]} {tahun}",
                    "umur": f"{umur_tahun} tahun dan {umur_bulan} bulan"
                })

            umur_bulan += 1
            if umur_bulan == 12:
                umur_bulan = 0
                umur_tahun += 1

    return hasil

# Function untuk menghitung umur menggunakan foreach loop
@router.post("/hitung-umur-for-each")
def hitung_umur_for_each(req: UmurRequest) -> List[Dict[str, str]]:
    hasil = []
    umur_tahun = req.tahun_mulai - req.tahun_lahir
    umur_bulan = req.bulan_mulai - req.bulan_lahir

    
    if umur_bulan < 0:
        umur_tahun -= 1
        umur_bulan += 12

    
    for tahun in range(req.tahun_mulai, req.tahun_akhir + 1):
        
        if tahun == req.tahun_mulai:
            bulan_awal = req.bulan_mulai
        else:
            bulan_awal = 1
        
        if tahun == req.tahun_akhir:
            bulan_akhir = req.bulan_akhir
        else:
            bulan_akhir = 12

        
        for bulan_index, bulan in enumerate(nama_bulan[bulan_awal - 1:bulan_akhir], start=bulan_awal):
            if bulan_index in req.bulan_yang_dipilih:
                hasil.append({
                    "pada": f"{bulan} {tahun}",
                    "umur": f"{umur_tahun} tahun dan {umur_bulan} bulan"
                })

            umur_bulan += 1
            if umur_bulan == 12:
                umur_bulan = 0
                umur_tahun += 1

    return hasil

# FUNNGSI while loop
@router.post("/hitung-umur-while")
def hitung_umur_while(req: UmurRequest) -> List[Dict[str, str]]:
    hasil = []
    tahun_sekarang = req.tahun_mulai
    bulan_sekarang = req.bulan_mulai
    umur_tahun = req.tahun_mulai - req.tahun_lahir
    umur_bulan = bulan_sekarang - req.bulan_lahir

   
    if umur_bulan < 0:
        umur_tahun -= 1
        umur_bulan += 12

    while (tahun_sekarang < req.tahun_akhir) or (tahun_sekarang == req.tahun_akhir and bulan_sekarang <= req.bulan_akhir):
        if bulan_sekarang in req.bulan_yang_dipilih:
            hasil.append({
                "pada": f"{nama_bulan[bulan_sekarang - 1]} {tahun_sekarang}",
                "umur": f"{umur_tahun} tahun dan {umur_bulan} bulan"
            })

        
        umur_bulan += 1
        bulan_sekarang += 1

        if bulan_sekarang > 12:  
            bulan_sekarang = 1
            tahun_sekarang += 1
            umur_tahun += 1

        if umur_bulan == 12:  
            umur_bulan = 0
            umur_tahun += 1

    return hasil
