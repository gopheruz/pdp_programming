PI = 3.1415

def Rings(r1, r2):
   s1 = PI * r1 *r1
   s2 = PI * r2 *r2
   if s2 > s1:
       return s2 - s1
   else:
       return s1 - s2

print(f"{Rings(12, 14):.2f}")
