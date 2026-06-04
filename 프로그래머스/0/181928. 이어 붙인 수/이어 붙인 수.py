def solution(num_list):
    even_ls = []
    odd_ls = []
    for n in num_list:
        even_ls.append(n) if n % 2 == 0 else odd_ls.append(n)
    even = "".join(map(str, even_ls))
    odd = "".join(map(str, odd_ls))
    return int(even) + int(odd)