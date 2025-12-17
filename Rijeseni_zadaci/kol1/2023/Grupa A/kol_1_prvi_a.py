'''
Napiši program koji definira vaš omiljeni film
i godinu izlaska filma.

Od korisika zatražiti upit kada je izašao
taj film npr. Koje godine je izašao film Kum?"

Ispisati "Točan odgovor!" ukoliko je odgovor točan.
Inače ispisati da je odgovor pogrešan uz informaciju
je li film izašao prije ili poslije unešene godine
i za koliko.
'''

omiljeni_film = 'The Prestige'
godina_izlaska = 2006

odgovor = int(input("Koje godine je izašao film " + omiljeni_film))
#odgovor = int(odgovor)
if odgovor == godina_izlaska:
    print("Tocan odgovor!")
else:
    print("Netocan odgovor!")
    if odgovor < godina_izlaska:
        print("Film je izasao", godina_izlaska-odgovor, "godina kasnije")
    else:
        print("Film je izasao ", odgovor-godina_izlaska, "godina ranije")
