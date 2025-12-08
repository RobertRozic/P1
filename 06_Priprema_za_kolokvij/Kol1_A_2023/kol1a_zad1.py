'''
Napiši program koji definira vaš omiljeni
film i godinu izlaska filma.

Od korisika zatražiti upit kada je
izašao taj film npr. Koje godine je izašao film Kum?"

Ispisati "Točan odgovor!"
ukoliko je odgovor točan.

Inače ispisati da je odgovor pogrešan
uz informaciju je li film izašao prije
ili poslije unešene godine i za koliko.
'''
film = "Prestige"
godina = 2006

unos = input("Koje godine je izasao film " + film + "?")
unos = int(unos)

if unos == godina:
    print("Tocan odgovor!")
else:
    print("Odgovor je pogresan!")
    if unos > godina:
        razlika = unos - godina
        print("Film je izasao " + str(razlika) + " godine prije unesene.")
    else:
        razlika = godina - unos
        print("Film je izasao " + str(razlika) + " godine nakon unesene.")
