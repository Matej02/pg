import requests

def convert_to_czk(amount, currency):
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    response = requests.get(url)
    if not response.ok:
        raise RuntimeError(f"Failed to fetch exchange rates. HTTP status code: {response.status_code}")
    exchange_data = response.text.splitlines()
    for line in exchange_data[2:]:
        fields = line.split('|')
        if len(fields) >= 5 and fields[3] == currency.upper():
            amount_in_czk = amount * float(fields[4].replace(',', '.')) / int(fields[2])
            return round(amount_in_czk, 2)
    raise ValueError(f"Currency {currency.upper()} not found in the exchange rate list.")

def main():
    try:
        user_input = input("Zadejte částku a měnu (např. '200 USD'): ")
        parts = user_input.split()
        if len(parts) != 2:
            raise ValueError("Špatný formát vstupu. Zadejte například '200 USD'.")
        amount = float(parts[0])
        currency = parts[1]
        result = convert_to_czk(amount, currency)
        print(f"{amount} {currency.upper()} = {result} CZK")
    except ValueError as e:
        print(f"Chyba: {e}")
    except RuntimeError as e:
        print(f"Chyba při přístupu ke kurzovnímu lístku: {e}")

if __name__ == "__main__":
    main()