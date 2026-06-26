def endirim_et(**kwargs):
    q=kwargs.get("qiymet" , 0 )
    yeni_qiymet=q-5

    print(f"Endirimli qiymet : {yeni_qiymet}")

endirim_et(mehsul= "Kofe", qiymet=15) 