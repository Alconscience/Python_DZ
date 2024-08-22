from smartphone import Smartphone

Smartphone1 = Smartphone(marka="Nokia", model="3310", number="+79891112233")
Smartphone2 = Smartphone(marka="Samsung", model="S20", number="+79892223344")
Smartphone3 = Smartphone(marka="Xiaomi", model="A20", number="+79893334455")
Smartphone4 = Smartphone(marka="Apple", model="iPhone 5", number="+79894445566")
Smartphone5 = Smartphone(marka="Honor", model="P420", number="+79895556677")

catalog = [Smartphone1, Smartphone2, Smartphone3, Smartphone4, Smartphone5]

for i in catalog:
    i.say_catalog()