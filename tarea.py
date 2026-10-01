paneles = int(input("¿Cuántos paneles solares hay? "))
potencia = float(input("¿Cuántos watts produce cada panel? "))
horas = float(input("¿Cuántas horas de sol hay? "))

energia = paneles * potencia * horas

print("La energía producida durante el día es:", energia, "Wh")