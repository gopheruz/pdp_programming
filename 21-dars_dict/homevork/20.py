countries_capitals = {
    "Afganistan": "Kobul",
    "Almanya": "Berlin",
    "Angola": "Luanda",
    "Argentina": "Buenos Aires",
    "Armaniston": "Yerevan",
    "Avstraliya": "Canberra",
    "Avstriya": "Vena",
    "Azerbayjon": "Boku",
    "Bahrin": "Manama",
    "Bangladesh": "Dakka",
    "Belgiya": "Brüssel",
    "Bolgariya": "Sofiya",
    "Braziliya": "Braziliya",
    "Bunday": "Addis-Abeba",
    "Buyuk Britaniya": "London",
    "Birma": "Naypyidav",
    "Bosniya va Gersegovina": "Sarayevo",
    "Vengriya": "Budapesht",
    "Vyetnam": "Xo Chi Min",
    "Gana": "Akra",
    "Germaniya": "Berlin",
    "Gvineya": "Konakri",
    "Gonduras": "Tegusigalpa",
    "Gollandiya": "Amsterdan",
    "Grenada": "Sent-Jordj",
    "Gruziya": "Tbilisi",
    "Gambiya": "Banjul",
    "Indoneziya": "Jakarta",
    "Ispaniya": "Madrid",
    "Italiya": "Roma",
    "Qatar": "Doha",
    "Qozog'iston": "Nursulton",
    "Qirg'iziston": "Bishkek",
    "Xitoy": "Pekin",
    "Yaponiya": "Tokio",
}

countries_capitals_europe_americas = {
    "France": "Paris",
    "Germany": "Berlin",
    "Brazil": "Brasilia",
    "Spain": "Madrid",
    "Italy": "Rome",
    "United Kingdom": "London",
    "Canada": "Ottawa",
    "USA": "Washington D.C.",
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "India": "New Delhi",
}

print("Original data:")
print(countries_capitals)
print(len(countries_capitals))
countries_capitals.update(countries_capitals_europe_americas)
print("\n\n\n\n\nYangilangan Data:")
print(countries_capitals)
print(len(countries_capitals))

