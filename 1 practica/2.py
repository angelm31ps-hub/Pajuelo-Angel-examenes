#Caso: REPORTE DE CALIFICACIONES

matemática = 17
ciencia = 14
historia = 15

peso_mate = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

#nota ponderada
nota_final = (matemática * peso_mate) + (ciencia * peso_ciencia) + (historia * peso_historia)

print("La nota final es:", round(nota_final, 1))

aprobado = nota_final >= 13.0
print("¿Aprobado?:", aprobado)

#resumen
estado = "Aprobado"
print(f"El estudiante obtuvo una nota final de {round(nota_final,1)} y su estado final es: {estado}")