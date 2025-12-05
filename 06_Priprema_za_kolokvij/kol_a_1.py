'''
Napiši program koji definira vaš omiljeni film
i godinu izlaska filma.

Od korisika zatražiti upit kada je izašao taj film
npr. Koje godine je izašao film Kum?"

Ispisati "Točan odgovor!" ukoliko je odgovor točan.
Inače ispisati da je odgovor pogrešan
uz informaciju je li film izašao prije ili poslije
unešene godine i za koliko.
'''

film = "Prestige"
godina = 2006

unos = int(input("Koje godine je izasao film " + film + "?"))

if unos == godina:
    print("Točan odgovor!")
else:
    print("Netočan odgovor!")
    
    if godina > unos:
        razlika = godina - unos
        print("Film je izasao", razlika, "godina nakon.")
    else:
        razlika = unos - godina
        print("Film je izasao", razlika, "godina prije.")
        
    print("Tocna godina:", godina)
