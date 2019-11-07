a = input("Masukkan Bilangan A :")
b = input("Masukkan Bilangan B :")
c = input("Masukkan Bilangan C :")

if a > b and a > c:
    terbesar = a
else:
    if b > c and b > a:
        terbesar = b
    else:
        terbesar = c

print("jadi bilangan yang terbesar adalah :",terbesar)