#El programas pregunta una frase y una letra.
frase = input("Introduce una frase: ")
letras = input("Introduce una letra")
contador = 0
for i in frase:
   if i == letra:
        contador += 1
        print("La letra '%s´ aparece %2 i veces en la frase ´%s´ . "  % (letra, contador, frase))
       
