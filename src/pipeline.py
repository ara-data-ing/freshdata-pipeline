# src/pipeline.py - Pipeline de ventas de FreshData Corp — el pipeline base del equipo

def cargar_ventas(archivo):
    """Carga datos de ventas desde un archivo CSV."""
    print(f"Cargando ventas desde: {archivo}")
    # Simulamos datos
    ventas = [
        {"tienda": "T001", "producto": "Leche", "cantidad": 150, "precio": 1.20},
        {"tienda": "T001", "producto": "Pan", "cantidad": 200, "precio": 0.80},
        {"tienda": "T002", "producto": "Leche", "cantidad": 90, "precio": 1.20},
        {"tienda": "T002", "producto": "Huevos", "cantidad": 75, "precio": 2.50},
    ]
    return ventas

def calcualr_total_tienda(ventas, tienda_id):
    """Calcula el total de ventas de una tienda."""
    total = 0
    for venta in ventas:
        if venta["tienda"] == tienda_id:
            total += venta["cantidad"] * venta["precio"]
    return total

if __name__ == "__main__":
    ventas = cargar_ventas("ventas_2024_01.csv")
    total = calcualr_total_tienda(ventas, "T001")
    print(f"Total tienda T001: ${total:.2f}")