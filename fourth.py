def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    def is_within_board(pos):
        return 1 <= pos[0] <= 8 and 1 <= pos[1] <= 8

    def is_clear_path(start, end, direction):
        current = (start[0] + direction[0], start[1] + direction[1])
        while current != end:
            if current in obsazene_pozice:
                return False
            current = (current[0] + direction[0], current[1] + direction[1])
        return True

    def get_direction(start, end):
        return (
            (end[0] - start[0]) // max(1, abs(end[0] - start[0])),
            (end[1] - start[1]) // max(1, abs(end[1] - start[1])),
        )

    if not is_within_board(cilova_pozice) or cilova_pozice in obsazene_pozice:
        return False

    typ = figurka["typ"]
    start = figurka["pozice"]

    if typ == "pěšec":
        if start[0] == 2 and cilova_pozice == (start[0] + 2, start[1]) and (start[0] + 1, start[1]) not in obsazene_pozice:
            return True
        return cilova_pozice == (start[0] + 1, start[1]) and cilova_pozice not in obsazene_pozice

    elif typ == "jezdec":
        row_diff, col_diff = abs(cilova_pozice[0] - start[0]), abs(cilova_pozice[1] - start[1])
        return (row_diff, col_diff) in [(2, 1), (1, 2)]

    elif typ == "věž":
        if start[0] == cilova_pozice[0] or start[1] == cilova_pozice[1]:
            direction = get_direction(start, cilova_pozice)
            return is_clear_path(start, cilova_pozice, direction)

    elif typ == "střelec":
        row_diff, col_diff = abs(cilova_pozice[0] - start[0]), abs(cilova_pozice[1] - start[1])
        if row_diff == col_diff:
            direction = get_direction(start, cilova_pozice)
            return is_clear_path(start, cilova_pozice, direction)

    elif typ == "dáma":
        row_diff, col_diff = abs(cilova_pozice[0] - start[0]), abs(cilova_pozice[1] - start[1])
        if start[0] == cilova_pozice[0] or start[1] == cilova_pozice[1] or row_diff == col_diff:
            direction = get_direction(start, cilova_pozice)
            return is_clear_path(start, cilova_pozice, direction)

    elif typ == "král":
        row_diff, col_diff = abs(cilova_pozice[0] - start[0]), abs(cilova_pozice[1] - start[1])
        return max(row_diff, col_diff) == 1

    return False
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 3), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (2, 3), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (4, 1), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (1, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (2, 1), obsazene_pozice))  # True

    print(je_tah_mozny(vez, (8, 5), obsazene_pozice))  # True
    print(je_tah_mozny(vez, (1, 8), obsazene_pozice))  # True
    print(je_tah_mozny(vez, (5, 8), obsazene_pozice))  # True
    print(je_tah_mozny(vez, (7, 8), obsazene_pozice))  # False

    print(je_tah_mozny(strelec, (4, 1), obsazene_pozice))  # True
    print(je_tah_mozny(strelec, (7, 4), obsazene_pozice))  # True
    print(je_tah_mozny(strelec, (8, 5), obsazene_pozice))  # True
    print(je_tah_mozny(strelec, (5, 4), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 4), obsazene_pozice))  # True
    print(je_tah_mozny(dama, (4, 7), obsazene_pozice))  # True
    print(je_tah_mozny(dama, (7, 3), obsazene_pozice))  # True
    print(je_tah_mozny(dama, (8, 8), obsazene_pozice))  # False

    print(je_tah_mozny(kral, (2, 4), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (1, 5), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (2, 3), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (1, 6), obsazene_pozice))  # False
