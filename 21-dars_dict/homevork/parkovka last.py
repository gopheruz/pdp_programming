import os
import random
n = int(input("Parkovka o'lchami: "))
parking_zone = [[1 for _ in range(n)] for _ in range(n)]
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0
parking_zone[random.randint(0,9)][random.randint(0,9)] = 0


while True:
    clear_console()
    print("Hozirgi parkovka holati:\n")
    for i in parking_zone:
        print(*i)
    
    row = int(input("\nQatorni kiriting: ")) - 1
    col = int(input("Ustunni kiriting: ")) - 1
    carname = input("Mashina: ")
    
    if parking_zone[row][col] == 0:
        parking_zone[row][col] = carname
        print(f"\n{carname} ({row+1}:{col+1}) manziliga joylashtirildi")
    else:
        print(f"\nBu yerda {parking_zone[row][col]} mashinasi turibdi.")
        print("Quyidagi joylar sizga eng yaqinlari:")
        empty_spaces = []
        for i in range(n):
            for j in range(n):
                if parking_zone[i][j] == 0:
                    distance = abs(i - row) + abs(j - col)
                    empty_spaces.append((distance, i, j))
        
        empty_spaces.sort() 
        recommended_spaces = empty_spaces[:10] 
        
        for distance, i, j in recommended_spaces:
            print(f"({i+1}:{j+1}) - Masofa: {distance}")
    
    continue_adding = input("\nYana mashina qo'yishni xohlaysizmi? (ha/yo'q): ").lower()
    if continue_adding != "ha":
        break

clear_console()
print("Oxirgi holat:\n")
for i in parking_zone:
    print(*i)
