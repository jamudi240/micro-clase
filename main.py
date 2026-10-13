# main.py - Sistema de Control de Inventario de Repuestos

def mostrar_menu():
    print("\n" + "="*40)
    print("   SISTEMA DE INVENTARIO - MULTIRESPUESTOS")
    print("="*40)
    print("1. Registrar nuevo repuesto")
    print("2. Visualizar repuestos en stock")
    print("3. Eliminar repuesto agotado")
    print("4. Salir")
    print("="*40)

def registrar_repuesto(inventario):
    print("\n--- REGISTRAR NUEVO REPUESTO ---")
    codigo = input("Ingrese el código OEM / Referencia: ").strip()
    nombre = input("Ingrese el nombre del repuesto: ").strip()
    
    try:
        cantidad = int(input("Ingrese la cantidad inicial: "))
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido para la cantidad.")
        return

    if codigo and nombre:
        inventario.append({"codigo": codigo, "nombre": nombre, "cantidad": cantidad})
        print(f"✅ Éxito: '{nombre}' (Código: {codigo}) registrado correctamente.")
    else:
        print("❌ Error: No se pueden ingresar campos vacíos.")

def visualizar_repuestos(inventario):
    print("\n--- LISTA DE REPUESTOS EN STOCK ---")
    if not inventario:
        print("⚠️ No hay repuestos registrados en el sistema.")
        return

    print(f"{'CÓDIGO':<15} | {'NOMBRE':<25} | {'CANTIDAD':<10}")
    print("-" * 55)
    for item in inventario:
        print(f"{item['codigo']:<15} | {item['nombre']:<25} | {item['cantidad']:<10}")

def main():
    inventario = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_repuesto(inventario)
        elif opcion == "2":
            visualizar_repuestos(inventario)
        elif opcion == "3":
            print("\n⏳ Función de eliminación asignada al Code Reviewer/Dev 3.")
        elif opcion == "4":
            print("\n👋 Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()