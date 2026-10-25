conteo = {}
with open("auth.log") as archivo:
    for linea in archivo:
        parte = linea.strip().split()
        ip = parte[-1]
        if ip in conteo:
            conteo[ip] = conteo[ip] + 1
        else:
            conteo[ip] = 1
for ip in conteo:
    if conteo[ip] >=3:
        print("posible ataque desde", ip, "-", conteo[ip], "intentos")