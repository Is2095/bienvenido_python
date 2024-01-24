
# Lambdas

# Es una función pero anónimas, son para funciones que no son de proposito general

suma_dos_valores = lambda primer_valor, segundo_valor: primer_valor + segundo_valor # en este caso creamos una función lambda, la cual recibe dos variables y va a retornar la suma de las dos varibles
print(suma_dos_valores(3, 8))

suma_dos_valores = lambda primer_valor, segundo_valor: print(primer_valor + segundo_valor) # en este casa la función no retorna nada solo imprime el resultado de la suma
print(suma_dos_valores(3, 8)) # este print va a tener como resultado none, ya que la función lambda no retorna nada

multiblicar_valores = lambda primer_valor, segundo_valor: primer_valor * segundo_valor - 4
print(multiblicar_valores(34, 65))

def suma_tres_valores(valor):
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + valor

print(suma_tres_valores(5)(8, 4))

