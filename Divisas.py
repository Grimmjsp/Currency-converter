# The currencies prices may be outdated

# Def function to convert from euros to dolars
def euros_dolares(amount):
    tasa = 1.18
    result = amount * tasa
    return result

# Def function to convert from euro to pounds
def euros_pounds(amount):
    tasa = 0.84
    result = amount * tasa
    return result

# Def function to convert from dolars to euros
def dolars_euros(amount):
    tasa = 0.85
    result = amount * tasa
    return result

# Def function to convert from dolars to pounds
def dolars_pounds(amount):
    tasa = 0.71
    result = amount * tasa
    return result

# Def function to convert from pounds to euros
def pounds_euros(amount):
    tasa = 1.18
    result = amount * tasa
    return result

# Def function to convert from pounds to dolars
def pounds_dolars(amount):
    tasa = 1.40
    result = amount * tasa
    return result


# Select currency to convert from
currency = input("Elige entre las siguientes divisas: Euros, Libras o Dólares.")

# Handle currency error
while currency is not ["Euros", "Libras", "Dólares"]:
    currency = input("Divisa no válida. Elige entre las siguientes divisas: Euros, Libras o Dólares.")

    # Conditions based on the currency from
    if currency.lower() == "euros":
        print("Euros -> Libras o Euros -> Dólares")
        conversor = input("Elección: ")

        # Handle selection error
        while conversor is not ["Libras", "Dólares"]:
            conversor = input("Divisa no válida. Selecciona Libras o Dólares.")
            amount = float(input("Cantidad de Euros: "))
            
            if conversor.lower() == "libras":
                conversion = euros_pounds(amount)
                print(f"La conversión de {amount} euros a libras es de {conversion} libras.")
            elif conversor.lower() == "dolares" or conversor.lower() == "dólares":
                conversion = euros_dolares(amount)
                print(f"La conversión de {amount} euros a dólares es de {conversion} dólares.")
                
    elif currency.lower() == "libras":
        print("Libras -> Euros o Libras -> Dólares")
        conversor = input("Elección: ")

        while conversor is not ["Euros", "Dólares"]:
            conversor = input("Divisa no válida. Selecciona Euros o Dólares.")
            amount = float(input("Cantidad de Libras: "))
            
            if conversor.lower() == "euros":
                conversion = pounds_euros(amount)
                print(f"La conversión de {amount} libras a euros es de {conversion} euros.")
            elif conversor.lower() == "dolares" or conversor.lower() == "dólares":
                conversion = pounds_dolars(amount)
                print(f"La conversión de {amount} libras a dólares es de {conversion} dólares.")
                
    elif currency.lower() == "dolares" or currency.lower() == "dólares":
        print("Dólares -> Euros o Dólares -> Libras")
        conversor = input("Elección: ")

        while conversor is not ["Euros", "Libras"]:
            conversor = input("Divisa no válida. Selecciona Euros o Libras.")
            amount = float(input("Cantidad de Dólares: "))
            
            if conversor.lower() == "euros":
                conversion = dolars_euros(amount)
                print(f"La conversión de {amount} dólares a euros es de {conversion} euros.")
            elif conversor.lower() == "libras":
                conversion = dolars_pounds(amount)
                print(f"La conversión de {amount} dolares a libras es de {conversion} libras.")
