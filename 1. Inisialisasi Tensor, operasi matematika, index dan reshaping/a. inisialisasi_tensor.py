import torch

"""

secara default tipe tensor adalah Long Tensor,
namun bisa kita rubah menjadi tipe lain dengan menggunakan fungsi

dtype=torch.float32

selain attribut tipe data ada atribut lain, seperti


device='cpu'/'cuda'

untuk menspesifikkan penggunaaan hardware, nilai defaultnya adalah cpu


requires_grad= True/false

nilai defaultnya adaah false, fungsi ini akan melacak operasi pada tensor
sehinggga akan menuntukkan nilai dari gradient nya.

"""

device = "cuda" if torch.cuda.is_available() else "cpu"

my_tensor = torch.tensor([[1,2,3], [4,5,6]], dtype=torch.float32, device = device, requires_grad=True)

print(my_tensor)
print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.shape) # mencetak ukuran dari tensor
print(my_tensor.requires_grad)


"""

operasi operasi tensor lain

.empty untuk membuat tensor kosong, benar benar kosong tanpa nilai
.zeros untuk membuat tensor bernilai 0 dengan ukuran  tertentu
.rand untuk membuat tensor random dengan nilai 0 - 1 (float)
.ones untuk membuat tensor bernilai 1
.eyes untuk membuat tensor yang bernilai  1 secara diagonal dan lainnyan akan bernilai 0
.arange fungsinya mirip seperti fungsi range di python (start, end, step)
.linspace untuk membuat tensor dengan nilai tertentu sejumlah steps yang di berikan (start, end, steps)
.normal_ untuk membuat tensor dengan nilai random yang berdistribusi normal (mean, std)
.uniform_ untuk membuat tensor dengan nilai random yang berdistribusi uniform (low, high)
.diag untuk membuat tensor diagonal

""" 

for i in range (50):
  print('-', end='')


x = torch.empty((3,3))
print(f'\n {x}')

x = torch.zeros(2,3)
print(x)

x = torch.rand(1,2)
print(x)

x = torch.ones(2,2)
print(x)

x = torch.eye(4,3)
print(x)

x = torch.arange(1, 7, 1)
print(x)

x = torch.linspace(1, 10, 5)
print(x)

x = torch.empty(3,3).normal_(mean=0, std=1)
print(x)

x = torch.empty(3,3).uniform_(0,1)
print(x)

x = torch.diag(torch.rand(3))
print(x)



for i in range (50):
  print('-', end='')

print('\n')

"""
cara menginisialisasi tensor dan melakuka konversi ke tipe lain seperti integer, float, double dan lain lain

"""

tensor = torch.arange(4)
print(tensor)

print(tensor.bool()) # konversi ke boolean
print(tensor.short()) # konversi ke short yang merupakan integer 16 bit
print(tensor.int()) # konversi ke integer 32 bit
print(tensor.long()) # konversi ke long yang merupakan integer 64 bit
print(tensor.half()) # konversi ke float 16 bit
print(tensor.float()) # konversi ke float 32 bit
print(tensor.double()) # konversi ke float 64 bit

# cara konversi tensor ke tipe data lain dan juga sebaliknya

import numpy as np
numpy_array = np.zeros((5,5))
tensor_from_numpy = torch.from_numpy(numpy_array) # konversi numpy array ke tensor
print(tensor_from_numpy)

numpy_from_tensor = tensor_from_numpy.numpy() # konversi tensor ke numpy array
print(numpy_from_tensor)