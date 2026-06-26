def uzun_sozler(*args):
    for soz in args:
        if len(soz) > 4 :
            print(soz)

uzun_sozler("ay", "aytac", "kod", "python", "dev")  # Ekrana "aytac" və "python" çıxmalıdır