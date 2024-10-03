# Funkce, která určuje, zda je číslo sudé nebo liché
def sudy_nebo_lichy(cislo):
    
    if cislo % 2 == 0:
        print("Číslo je sudé")  # Výpis informace o sudém čísle
    else:
        # Pokud není zbytek 0, číslo je liché
        print("Číslo je liché")  # Výpis informace o lichém čísle

# Nyní budeme testovat naši funkci s různými čísly

# Test 1: Zkontrolujeme číslo 3
sudy_nebo_lichy(3)  # Očekáváme, že to vypíše "Číslo je liché"

# Test 2: Zkontrolujeme číslo 1000000
sudy_nebo_lichy(1000000)  # Očekáváme, že to vypíše "Číslo je sudé"
