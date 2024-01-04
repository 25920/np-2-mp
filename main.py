import numpy as np 

d_complex = [
    [1,5j,9j],
    [-5j,82,1-1j],
    [-9j,1+1j,-9]
]

print("D is a complex matrix with size 3 by 3\n")
for k in d_complex:
    r = []
    for j in k:
        r.append(complex(j))
    print(np.array(r))
    # print(np.array(r).real)
    # print(np.array(r).imag)
print("########################################\n")

d_conjugate = []

for i in range(len(d_complex)):
    row = []
    for k in d_complex[i]:
        row.append(np.conjugate(k))
    d_conjugate.append(row)

print("D's Conjugaate form\n")
for k in d_conjugate:
    r = []
    for j in k:
        r.append(complex(j))
    print(np.array(r))
print("########################################\n")

d_transpose = np.transpose(d_conjugate)

print("D's conjuate transpose: transpose after conjugation'\n")
for k in d_transpose:
    r = []
    for j in k:
        r.append(complex(j))
    print(np.array(r))
print("########################################\n")

if (d_transpose==d_complex).all():
    print("As D == D's transpose:")
    print("D is a hermitian matrix")
    print("########################################\n")
