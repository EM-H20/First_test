import os

file_path = "C:/Users/홍의민/Desktop/FiLE_Rename/윤쌤이 준거찬송가 - 복사본" #바꿀 파일 A
file_path_abs = [os.path.join(file_path, i) for i in os.listdir(file_path)]

file_path_old = "C:/Users/홍의민/Desktop/FiLE_Rename/찬송가" #바꿀 파일의 이름 B
file_path_old_abs = [os.path.join(file_path_old, i)for i in os.listdir(file_path_old)]

for file, file_old in zip(file_path_abs, file_path_old_abs):
    dir_path = os.path.dirname(file) #절대경로
    file_name = os.path.basename(file) #파일의 이름 ex) new000
    file_name_old = os.path.basename(file_old) #파일의 예전 이름 ex) 만복의 근원

    file_name_new = file_name.replace(file_name, file_name_old) #앞에 이름을 뒤의 이름으로 바꿈
    os.rename(file, os.path.join(dir_path, file_name_new)) #파일 경로와 이름 합치기 -끝-