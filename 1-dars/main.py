destonation = int(input("Uyingizdan ishxonagacha necha km: "))
UserMoney = int(input("Qancha pulingiz bor: "))
TaxiPeerKM = int(input("Taxi 1 kM ga mechpul: "))
BusPrice = int(input("Aftobus nechpul: "))
busCount = int(input("Nechta aftobusda borasiz: "))

TaxiPrice = destonation * TaxiPeerKM
print(f"taxida Ketaolasizmi {TaxiPrice <= UserMoney}")
print(f"Aftobusda ketaolasizmi {UserMoney >= (BusPrice*busCount)}")