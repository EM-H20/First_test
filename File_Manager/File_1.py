import os

file_path = "C:/Users/홍의민/Desktop/FiLE_Rename/윤쌤이 준거찬송가1" #바뀌는 이름
file_path_abs = [os.path.join(file_path, i) for i in os.listdir(file_path)]

k = [i for i in range(1, 646)]

for i, j in zip(file_path_abs, k):
    dir_path = os.path.dirname(i)
    file_name = os.path.basename(i)

    Stx = '{}'.format(j)

    file_new = file_name.replace(Stx + '장', Stx.zfill(3) + '장') 
    print(Stx, Stx.zfill(3))
    #자릿수 - 3 ex) 1장 -> 자릿수 3 - 1 = 2 0앞에 2개 -> 001장
    
    os.rename(i, os.path.join(dir_path, file_new))