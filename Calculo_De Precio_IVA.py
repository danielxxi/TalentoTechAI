# Marcela Vargas
# Edwin
# José Daniel Ayala Barrera



def main():
    articulo = input("Articulo: ")
    cantidad = int(input("Cantidad: "))
    precio_con_iva = float(input("Precio unitario (con IVA): $"))
    porcentaje_iva = float(input("Porcentaje del IVA: "))
    
    precio_sin_iva = precio_con_iva / (1 + porcentaje_iva / 100)
    subtotal = cantidad * precio_sin_iva
    valor_iva = cantidad * precio_sin_iva * (porcentaje_iva / 100)
    total_con_iva = subtotal + valor_iva
    
    
    print(f"\nArticulo: {articulo}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario (Con IVA): ${precio_con_iva:.2f}")
    print(f"Precio unitario (Sin IVA): ${precio_con_iva / (1 + porcentaje_iva / 100):.2f}")    
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA: {porcentaje_iva:}%: ${valor_iva:.2f}")
    print(f"Total: ${total_con_iva:.2f}")
if __name__ == "__main__":
    main()