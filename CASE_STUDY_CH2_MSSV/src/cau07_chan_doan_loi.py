ma_may = input("Nhập mã máy: ")
cong_suat_w = int(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

ma_mav = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Đã sửa: chuyển sang float để tính toán chính xác
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_mav}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# ==========================================
# CÁC LỖI ĐÃ PHÁT HIỆN VÀ ĐÃ SỬA:
# 1. Lỗi kiểu dữ liệu (TypeError): Biến cong_suat_w ban đầu nhận giá trị từ hàm input() 
#    là kiểu chuỗi (str), dẫn đến khi tính toán điện năng sẽ gây lỗi không nhân được với số phút.
#    -> Khắc phục: Ép kiểu dữ liệu sang float (hoặc int).
# 2. Lỗi định dạng f-string (Syntax/Formatting Error): Dòng in điện năng ban đầu viết nhầm 
#    thành `{dien_nang:..3f}` (thừa dấu chấm). 
#    -> Khắc phục: Sửa lại thành `{dien_nang_kwh:.3f}` đúng chuẩn định dạng số thập phân.
# ==========================================

ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")   # KHÔNG dùng float hay int ở đây
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")