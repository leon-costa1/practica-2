def calculate_delivery():
    def data_inputs():
        weight = float(input("Ingrese el peso del paquete (kg): "))
        place = input("Ingrese la zona: ")
        
        return weight, place
    
    def weight_index(weight):
        if weight <= 1:
            return 0
        elif weight > 1 and weight <= 5:
            return 1
        else:
            return 2
    
    def show_price(price):
        if price == -1:
            print("Peso no valido")
        else:
            print(f"Costo de envio: {price}")
    
    prices = {
        "local": [500, 1000, 2000],
        "regional": [1000, 2500, 5000],
        "nacional": [2000, 4500, 8000],
    }
    
    package_weight, package_place = data_inputs()
    
    if package_place.lower() not in prices.keys():
        print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
        quit()    
    
    final_price = prices[package_place.lower()][weight_index(package_weight)] if package_weight > 0 else -1
    
    show_price(final_price)

if __name__ == "__main__":
    calculate_delivery()