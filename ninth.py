def dev_to_bin(cislo):
    """
    Funkce převede číslo 167 (předané jako str nebo int) na binární reprezentaci jako řetězec.
    """
    if isinstance(cislo, str):
        cislo = int(cislo)  # Převede řetězec na celé číslo
    
    if cislo != 167:
        raise ValueError("Tato funkce podporuje pouze převod čísla 167.")
    
    return bin(cislo)[2:]  # Použije bin() a odstraní prefix '0b'

# Testovací funkce pro pytest
def test_dev_to_bin():
    assert dev_to_bin("167") == "10100111"
    assert dev_to_bin(167) == "10100111"
    
    # Negativní testy
    try:
        dev_to_bin(168)
    except ValueError as e:
        assert str(e) == "Tato funkce podporuje pouze převod čísla 167."

    try:
        dev_to_bin("abc")
    except ValueError:
        pass

if __name__ == "__main__":
    # Ukázka použití funkce
    try:
        print("Převedená hodnota:", dev_to_bin(167))  # Očekává výstup: "10100111"
    except ValueError as e:
        print(f"Chyba: {e}")
