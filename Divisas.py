# The currencies prices may be outdated

# Prices for exchange
exchange_rates = {
    "euros": {"libras": 0.84, "dolares": 1.18},
    "libras": {"euros": 1.18, "dolares": 1.40},
    "dolares": {"euros": 0.85, "libras": 0.71}
}

# Currencies to work with
currencies = ["euros", "libras", "dolares"]
# Function to trade
def exchange(currency_from, currency_to, amount):
    price = exchange_rates[currency_from.lower()][currency_to.lower()]
    result = price * amount
    return result

# Additional info
print("!Bienvenido¡\n")
print("Los precios pueden estar desactualizados.\n")
print("En cualquier momento, puede escribir 'salir' para detener el programa.\n")

print("[!]" + "-"*100 + "[!]")

while True:
    currency_from = input("Trabajamos con Euros, Libras y Dolares.\n¿Con qué divisa quiere trabajar hoy? ")
    if currency_from.lower() == "salir":
        print("[*] Finalizando... !Hasta luego¡")
        break
    elif currency_from.lower() not in currencies:
        print("Divisa no válida. Inténtalo de nuevo.")
        continue
    print(f"Ha escogido trabajar con {currency_from.capitalize()}")
    
    amount = None
    while amount is None:
        try:
            amount = float(input(f"Cantidad de {currency_from.lower()}: "))
        except ValueError:
            print("[!] Error... Por favor, introduzca un número.")
            continue
        
    currency_to = input(f"¿A qué divisa quiere convertir {amount} {currency_from.lower()}? ")
    if currency_to.lower() not in currencies:
        print("Divisa no válida. Inténtalo de nuevo.")
        continue
    
    result = exchange(currency_from, currency_to, amount)
    print(f"-> {amount} {currency_from} equivale a {result} {currency_to}")