import os

# Parkovka zonasi
parking_zone = [[0 for _ in range(10)] for _ in range(10)]

while True:
    os.system("clear")
    print("\nHozirgi parkovka holati:")
    for row in parking_zone:
        for cell in row:
            print(cell if cell != 0 else ".", end=" ")
        print()

    # Foydalanuvchidan markazni so'rash
    row = int(input("Markaz qatori (1-10): ")) - 1
    col = int(input("Markaz ustuni (1-10): ")) - 1

    if parking_zone[row][col] == 0:
        car_name = input("Mashina nomini kiriting: ")
        parking_zone[row][col] = car_name
        print(f"{car_name} mashinasi ({row+1}, {col+1}) joyga qo'yildi.")
    else:
        print(f"({row+1}, {col+1}) manzil band!")
        print("Bo'sh joylar qidirilmoqda...")

        # Markazdan bo'sh joy qidirish
        empty_spots = []
        for distance in range(1, 10):  # Maksimal masofa 10
            for dr in range(-distance, distance + 1):
                for dc in range(-distance, distance + 1):
                    new_row = row + dr
                    new_col = col + dc
                    if (
                        0 <= new_row < 10 and
                        0 <= new_col < 10 and
                        parking_zone[new_row][new_col] == 0
                    ):
                        empty_spots.append((new_row, new_col))
                        if len(empty_spots) == 5:  # Faqat 5 ta joyni yig'ish
                            break
            if len(empty_spots) == 5:
                break
        if empty_spots:
            print("\nTavsiya qilingan bo'sh joylar:")
            for idx, (er, ec) in enumerate(empty_spots):
                print(f"{idx+1}. ({er+1}, {ec+1})")
            closest_spot = empty_spots[0]  # 1-joy eng yaqin deb olinadi
            print(f"\nEng yaqin joy: ({closest_spot[0]+1}, {closest_spot[1]+1})")
            response = input("Ushbu joyga mashina qo'yasizmi? (ha/yo'q): ").lower()
            if response == "ha":
                car_name = input("Mashina nomini kiriting: ")
                parking_zone[closest_spot[0]][closest_spot[1]] = car_name
                print(f"{car_name} mashinasi ({closest_spot[0]+1}, {closest_spot[1]+1}) joyga qo'yildi.")
        else:
            print("Bo'sh joy topilmadi!")

    continue_parking = input("Mashinalarni joylashda davom etasizmi? (ha/yo'q): ").lower()
    if continue_parking != "ha":
        break

print("\nOxirgi parkovka holati:")
for row in parking_zone:
    for cell in row:
        print(cell if cell != 0 else ".", end=" ")
    print()
