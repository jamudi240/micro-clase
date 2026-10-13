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
    codigo = input("Ingrese el código OEM / Referencia: ").strip()
    nombre = input("Ingrese el nombre del repuesto: ").strip()
    if codigo and nombre:
        inventario.append({"codigo": codigo, "nombre": nombre})
        print(f"✅ Éxito: '{nombre}' registrado correctamente.")
    else:
        print("❌ Error: No se pueden ingresar campos vacíos.")

def main():
    inventario = []
    mostrar_menu()

if __name__ == "__main__":
    main()