#!/usr/bin/python3
telebeler= {
    "Aytac" : 95,
    "Ali" :48,
    "Leyla" : 75,
    "Mamed" :35,
    "Zaur" : 82
    }

def neticeni_yoxla(bal):
    if bal >= 51:
        return "Kecdi" 
    else:
        return "Kesildi"
    
print("---Telebe neticeleri hesabati---")

for ad, bal in telebeler.items():
   
   durum=neticeni_yoxla(bal)
   print(f"Telebe: {ad}, Bal: {bal}, Durum: {durum}")