def to_base_3(n):
    res = ''
    while n:
        res = str(n % 3)+res
        n //= 3
    return res

max_R = 0
for N in range(1, 200):
    tri_N = to_base_3(N)
    
    if N % 3 == 0:
        if len(tri_N) >= 2:
            result_tri = tri_N + tri_N[-2:]
        else:
            result_tri = tri_N+tri_N[-1]*2
    else:
        rem = N % 3
        rem_x5 = rem * 5
        rem_tri = to_base_3(rem_x5)
        result_tri = tri_N + rem_tri
    
    R = 0
    for digit in result_tri:
        R = R * 3 + int(digit)
    
    if R <= 173 and R > max_R:
        max_R = R

print(max_R)
