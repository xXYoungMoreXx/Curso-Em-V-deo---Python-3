print("="*30)
t1 = (int(input('Digite um número inteiro: ')))
print("="*30)
for t in range(2, 10):
    print("{:2}{:^5}{:2}{:^4}{}".format(t1, "x", t, "=", (t1*t)))
