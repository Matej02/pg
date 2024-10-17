def cislo_text(cislo):
    # Definice seznamů pro jednotky, desítky a teen čísla
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    teens = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    # Podmínky pro převod čísel do textové formy
    cislo = int(cislo)  # Převod na celé číslo
    if cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return teens[cislo - 10]
    elif 20 <= cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return f"{desitky[desitka]} {jednotky[jednotka]}"
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah (0-100)"

# Testování funkce
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")  # Zadej číslo
    text = cislo_text(cislo)  # Převod čísla na text
    print(text)  # Výstup textové reprezentace