# 수탉은 5달러 암닭은 3달러 병아리는 3마리 1달러 100달러사용하여 닭 100마리를 사려면 몇마리 수탉 암탉 병아리
# a+b+3*c=100
# 5a+3b+c = 100

dollar = 100
max = 100
ac,bc,cc = 5,3,3
for a in range(0,dollar//ac +1):
    for b in range(0,dollar//bc +1):
        for c in range(0,max//cc +1):
            if a+b+3*c == max and 5*a+3*b+c == dollar:
                print(f"수탉 : {a}, 암탉 : {b}, 병아리 : {3*c}")