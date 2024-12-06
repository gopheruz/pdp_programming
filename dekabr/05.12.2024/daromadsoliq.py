daromatsoliq = lambda maosh, soliqFoizi: maosh * (soliqFoizi / 100)


toladaromad = lambda maosh, soliqFoizi:( maosh - (daromatsoliq(maosh, soliqFoizi)))


salary = int(input("Maosh: "))

print(f"{daromatsoliq(salary, 12)}")
print(f"{toladaromad(salary, 12)}")


