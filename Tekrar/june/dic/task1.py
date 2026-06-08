#!/usr/bin/python3

menyu = {
    "Kabab" : 10,
    "Plov" : 8,
    "Dolma" : 7,
    "Sup" : 4
}

for yemek,qiymet in menyu.items():

    yeni_qiymet = qiymet + 2

    print(f"{yemek} qiymetinin yeni qiymeti: {yeni_qiymet} AZN")