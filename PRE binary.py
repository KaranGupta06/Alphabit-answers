num, base_num = input().split()
base_num = int(base_num)
base_fin = int(input())

num_base10 = 0
for i, j in enumerate(num[::-1]):
    num_base10 += int(j) * (base_num**i)

def binary(num, base):
    final = ""

    if num == 0:
        return 0
    
    while num != 0:
        num, a = divmod(num, base)
        final = str(a) + final

    return final

print(binary(num_base10, base_fin))