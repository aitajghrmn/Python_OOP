def radara_dusenler(**kwargs):
    for acar , deyer in kwargs.items():
        if deyer > 90 :
            print(f"{acar} radara dusdu")

radara_dusenler(BMW=120, MERCEDES=85 , TOYOTA=140, OPEL=70)