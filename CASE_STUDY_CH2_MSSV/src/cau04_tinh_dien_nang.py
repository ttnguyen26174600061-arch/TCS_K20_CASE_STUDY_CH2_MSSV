cong_suat_w = 250
so_phut = 60
don_gia_vnd_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi_vnd = dien_nang_kwh * don_gia_vnd_kwh
print("Cong suat (W):", cong_suat_w)
print("Thoi gian (phut):", so_phut)
print("Don gia (VND/kWh):", don_gia_vnd_kwh)
print("Dien nang (kWh):", dien_nang_kwh)
print("Chi phi (VND):", chi_phi_vnd)
print("Kieu du lieu dien nang:", type(dien_nang_kwh))
print("Kieu du lieu chi phi:", type(chi_phi_vnd))
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi_vnd = dien_nang_kwh * don_gia_vnd_kwh
print("Dien nang khi dung 60 phut:", dien_nang_kwh)
print("Chi phi khi dung 60 phut:", chi_phi_vnd)