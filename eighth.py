def bin_to_dec(binarni_cislo):
    """
    Funkce, která konvertuje binární číslo na decimální.
    Binární číslo může být předáno jako str nebo int.
    """
    # Ujistěte se, že číslo je ve stringové podobě
    binarni_cislo = str(binarni_cislo)
    # Použijte int() s druhým parametrem 2 pro převod z binární soustavy
    return int(binarni_cislo, 2)


def test_funkce():
    # Testy pro funkci bin_to_dec()
    assert bin_to_dec("0") == 0          # Test pro binární 0
    assert bin_to_dec(1) == 1            # Test pro binární 1
    assert bin_to_dec("100") == 4        # Test pro binární "100" (4 v desítkové soustavě)
    assert bin_to_dec(101) == 5          # Test pro binární 101 (5 v desítkové soustavě)
    assert bin_to_dec("010101") == 21    # Test pro binární "010101" (21 v desítkové soustavě)
    assert bin_to_dec(10000000) == 128   # Test pro binární 10000000 (128 v desítkové soustavě)
    assert bin_to_dec("10011101") == 157 # Test pro binární "10011101" (157 v desítkové soustavě)
    print("Všechny testy prošly.")


if __name__ == "__main__":
    # Spustíme testy
    test_funkce()
    
    # Zobrazíme výstupy pro konkrétní binární čísla
    print(bin_to_dec("10011101"))  # Očekává se výstup 157
    print(bin_to_dec(10011101))    # Očekává se výstup 157
