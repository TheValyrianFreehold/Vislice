import random

ZACETEK = "z"

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA, PORAZ = "W", "X"

class Igra(object):
    def __init__(self, geslo, crke = []):
        self.geslo = geslo
        self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka.upper() not in self.geslo.upper()]
    
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka.upper() in self.geslo.upper()]

    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def pravilni_del_gesla(self):
        return "".join([c if c in self.crke else "_" for c in self.geslo.upper()])
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            return NAPACNA_CRKA

with open("besede.txt", encoding="utf-8") as f:
    bazen_besed = f.read().split()

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)