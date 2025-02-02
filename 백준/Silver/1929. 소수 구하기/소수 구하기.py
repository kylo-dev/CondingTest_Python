def calc_prime(m,n):
  check = [1 for i in range(n+2)]
  i = 2
  k = 2
  while i <= n:
    if check[i] == 1:
      while i*k <= n :
        check[i*k] = 0
        k += 1
      k = 2
    i += 1
  check[1] = 0
  while m <= n :
    if check[m] == 1:
      print(m)
    m += 1

m, n =map(int, input().split())
calc_prime(m, n)