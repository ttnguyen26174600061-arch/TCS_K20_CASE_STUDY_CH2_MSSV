from datetime import datetime
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat (W): "))
so_phut = int(input("Nhap thoi gian su dung (phut): "))
don_gia_vnd_kwh = float(input("Nhap don gia (VND/kWh): "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi_vnd = dien_nang_kwh * don_gia_vnd_kwh
vuot_60_phut = so_phut > 60
thoi_gian = datetime.now()
print("\n--- THONG TIN PHIEN SU DUNG ---")
print("Ma phien:", ma_phien)
print("Ma may:", ma_may)
print("Cong suat (W):", cong_suat_w)
print("Thoi gian su dung (phut):", so_phut)
print("Don gia (VND/kWh):", don_gia_vnd_kwh)
print("Dien nang (kWh):", dien_nang_kwh)
print("Chi phi (VND):", chi_phi_vnd)
print("Su dung tren 60 phut:", vuot_60_phut)
print("Thoi gian ghi nhan:", thoi_gian)