import torch

x = torch.tensor([1,2,3] )
y = torch.tensor([9,8,7])


# Penjumlahan

"""

ada 2 cara yang bisa dilakukan untuk menjumlahkan tensor
1. menggunakan operator +
2. menggunakan fungsi torch.add()

"""

jumlah= torch.empty(3)
torch.add(x, y, out=jumlah)

jumlah2 = torch.empty(3)
jumlah2 = x + y

print(f'hasil penjumlahan {jumlah}, formatnya adalah {jumlah.dtype}')
print(f'hasil penjumlahan {jumlah2}, formatnya adalah {jumlah2.dtype}')


# Pengurangan

for i in range (50):
  print('-', end='')

print('\n')

"""

ada 2 cara yang bisa dilakukan untuk mengurangkan tensor
1. menggunakan operator -
2. menggunakan fungsi torch.sub()

"""


kurang= torch.empty(3)
torch.sub(x, y, out=kurang) 
print(f'hasil pengurangan {kurang}, formatnya adalah {kurang.dtype}')

kurang2 = torch.empty(3)
kurang2 = x - y
print(f'hasil pengurangan {kurang2}, formatnya adalah {kurang2.dtype}')

# Pemabagian

for i in range (50):
  print('-', end='')

print('\n')

"""

metode pembagian tensor ada 3 jenis berbeda
1. pembagian elemen per elemen (element-wise division) menggunakan operator / atau fungsi torch.div()
2. pembagian skalar (scalar division) menggunakan operator / atau fungsi torch.div()
3. pembagian elemen per elemen dengan pembulatan ke bawah (floor division) menggunakan fungsi torch.floor_divide()

"""

pembagian = torch.empty(3)

pembagian0 = torch.true_divide(x, y, out=pembagian)
print(f'hasil pembagian {pembagian}, formatnya adalah {pembagian.dtype}')

pembagian2 = x / y
print(f'hasil pembagian {pembagian2}, formatnya adalah {pembagian2.dtype}')

pembagian3 = x // y
print(f'hasil pembagian {pembagian3}, formatnya adalah {pembagian3.dtype}')

pembagian4 = x / 2
print(f'hasil pembagian {pembagian4}, formatnya adalah {pembagian4.dtype}')


# Inplace Operation

for i in range (50):
  print('-', end='')

print('\n')

"""

inplace operation, merupakan operasi yang langsung mengubah nilai tensor tanpa harus membuat tensor baru,
ada beberapa metode untuk melakukan inplace operation, yaitu dengan:
1. menambahkan underscore (_) pada fungsi operasi, misal: add_(), sub_(), mul_(), div_() dan lain lain
2. menggunakan operator dengan tanda sama dengan, misal: +=, -=, *=, /=
3. menggunakan variabel, seperti x = x + y


"""

t = torch.zeros(3)
print(f'sebelum inplace operation {t}')

t.add_(y)
print(f'sesudah inplace operation {t}')

t += y
print(f'sesudah inplace operation {t}')

t = t + y
print(f'sesudah inplace operation {t}')

# perpangkatan

"""

perpangkatan pada tensor bisa dilakukan dengan 2 cara
1. menggunakan operator **
2. menggunakan fungsi torch.pow()

"""

for i in range (50):
  print('-', end='')

print('\n')


pangkat = torch.arange(1,4)
print(f'sebelum perpangkatan {pangkat}')    

pangkat2 = torch.empty(3)
torch.pow(pangkat, 2, out=pangkat2)
print(f'sesudah perpangkatan {pangkat2}')

pangkat3 = pangkat ** 2
print(f'sesudah perpangkatan {pangkat3}')


#Perbandingan
for i in range (50):
  print('-', end='')    

print('\n')

"""
perbandingan pada tensor sama seperti operasi perbandingan pada python secara umum,
yang perlu di garis bawahi adalah perbandingannya adalah elemen per elemen (element-wise comparison)

"""

perbandingan = x > y
print(f'hasil perbandingan antara x dan y adalah {perbandingan}')

perbandingan2 = x < y
print(f'hasil perbandingan antara x dan y adalah {perbandingan2}')


# Perkalian Matrix
for i in range (50):
  print('-', end='')    

print('\n')


"""

perkalian matrix pada tensor bisa dilakukan dengan 3 cara
1. menggunakan fungsi nama_matrixx.mm()
2. menggunakan fungsi torch.matmul()
3. menggunakan fungsi torch.mm()

mm adalah singkatan dari matrix multiplication yang hanya bisa digunakan untuk matrix 2 dimensi
untuk matriks yang berdimensi lebih dari 2, bisa menggunakan torch.matmul()

"""
x1 = torch.rand(2,3)
y1 = torch.rand(3,2)

matrix1 = x1.mm(y1)
print(f'hasil perkalian matrix 1 adalah {matrix1}')

matrix2 = torch.matmul(x1, y1)
print(f'hasil perkalian matrix 2 adalah {matrix2}')

matrix3 = torch.mm(x1, y1)
print(f'hasil perkalian matrix 3 adalah {matrix3}')



# Matrix Exponentiation

for i in range (50):
  print('-', end='')    

print('\n')


"""
matrix exponentiation adalah operasi perpangkatan pada matrix, dimana matrix harus berbentuk persegi (n x n)
jadi nantinya tiap elemen akan di kalikan sesuai dengan jumlah pangkatnya dan akan di jumlahkan

"""

matrix_exp = torch.tensor([[2,3],
                           [4,5]])

print(f'sebelum matrix exponentiation adalah {matrix_exp}')

matrix_exp2 = torch.matrix_power(matrix_exp, 3)
print(f'hasil matrix exponentiation adalah {matrix_exp2}')


# Matrix wise multiplication

for i in range (50):
  print('-', end='')    

print('\n')

