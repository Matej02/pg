def je_prvocislo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    prvocisla = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla

if __name__ == "__main__":
    cislo = int(input("Zadej číslo pro kontrolu prvočísla: "))
    print(f"Je číslo {cislo} prvočíslo? {je_prvocislo(cislo)}")
    
    maximum = int(input("Zadej maximum pro seznam prvočísel: "))
    print(f"Prvočísla mezi 1 a {maximum}: {vrat_prvocisla(maximum)}")
