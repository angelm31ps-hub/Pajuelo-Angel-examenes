#Calculadora de propinas

"datos"

total_cuenta = float(input("Total de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina: "))
num_personas = int(input("Número de personas: "))

#calculo

monto_propina = total_cuenta * (porcentaje_propina / 100)
monto_total = total_cuenta + monto_propina
monto_por_persona = monto_total / num_personas

print(f"Monto total con propina: S/. {monto_total:.2f}")
print(f"Cada persona debe pagar: S/. {monto_por_persona:.2f}")

if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")