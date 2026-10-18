from datetime import datetime

# Nhap thong tin phien su dung phong may
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat (W): "))
so_phut = int(input("Nhap thoi gian su dung (phut): "))
don_gia_vnd_kwh = float(input("Nhap don gia (VND/kWh): "))
# Tinh dien nang tieu thu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

# Tinh chi phi su dung dien
chi_phi_vnd = dien_nang_kwh * don_gia_vnd_kwh

# Kiem tra thoi gian su dung
vuot_60_phut = so_phut > 60

# Ghi nhan thoi diem
thoi_gian_ghi_nhan = datetime.now()
thoi_gian_text = thoi_gian_ghi_nhan.strftime("%Y-%m-%d %H:%M:%S")

# Hien thi ket qua
print("\n===== LAB USAGE RECORD =====")
print(f"Ma phien: {ma_phien}")
print(f"Ma may: {ma_may}")
print(f"Cong suat: {cong_suat_w:.2f} W")
print(f"Thoi gian su dung: {so_phut} phut")
print(f"Don gia: {don_gia_vnd_kwh:.2f} VND/kWh")
print(f"Dien nang tieu thu: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi_vnd:.2f} VND")
print(f"Su dung tren 60 phut: {vuot_60_phut}")
print(f"Thoi diem ghi nhan: {thoi_gian_text}")