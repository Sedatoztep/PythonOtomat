items_in_stock = [
    {
        "item_id": 0,
        "item_name": "Adana Dürüm",
        'item_price': 50,
    },
    {
        "item_id": 1,
        "item_name": "Ice Tea",
        'item_price': 10,
    },
    {
        "item_id": 2,
        "item_name": "Piskevit",
        'item_price': 15,
    },
    {
        "item_id": 3,
        "item_name": "Muzlu Süt",
        'item_price': 35,
    },
    {
        "item_id": 4,
        "item_name": "Bici Bici",
        'item_price': 40,
    },
]

the_item = []

reciept = """
\t\tÜRÜNLER -- FİYAT
"""

sum = 0

run = True

print("------- PYTHON OTOMAT -------\n\n")
print("----------Stocktaki Ürünler----------\n\n")

for i in items_in_stock:
    print(f"Ürün: {i['item_name']} --- Fiyat: {i['item_price']} --- Ürün No: {i['item_id']}")


def machine(items_in_stock, run, the_item):
    while run:

        buy_item = int(input("\n\nSatın almak istediğiniz ürünün ürün kodunu girin: "))

        if buy_item < len(items_in_stock):
            the_item.append(items_in_stock[buy_item])
        else:
            print("YANLIŞ ÜRÜN ID!")

        more_items = str(input("daha fazla öğe eklemek için herhangi bir tuşa basın ve çıkmak için q tuşuna basın.. "))

        if more_items == "q":
            run = False

    rec_bool = int(input(("1. Fişinizi yazdırın 2. yalnızca toplam tutarı yazdırın .. ")))
    if rec_bool == 1:
        print(create_reciept(the_item, reciept))
    elif rec_bool == 2:
        print(sum(the_item))
    else:
        print("GEÇERSİZ GİRİŞ")


def sum(the_item):
    sum = 0

    for i in the_item:
        sum += i["item_price"]

    return sum


def create_reciept(the_item, reciept):
    for i in the_item:
        reciept += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """

    reciept += f"""
        \tTotal --- {sum(the_item)}


        """
    return reciept


if __name__ == "__main__":
    machine(items_in_stock, run, the_item)
