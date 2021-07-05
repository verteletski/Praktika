import random

ls = [random.randrange(-100, 100) for i in range(30)]

print(f"Generated list: {ls}\n")

max_elem = (max(ls), ls.index(max(ls)))

print(f"Max element: {max_elem[0]}\t\tindex:{max_elem[1]}\n")

new_ls = list(filter((lambda i: i & 1 == 1), ls))

print(f"Odd list: ", end='')
if new_ls:
    new_ls.sort(key=lambda i: -i)
    print(new_ls)
else:
    print("odd elements not found")
