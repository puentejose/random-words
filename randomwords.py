import random

WORDS = ("Boleto", "sidra", "sueño", "Dragón", "Carro",  "lavamanos", "Colador", "Cine", "Gladiador",
         "computadora", "celular", "Lapiz", "pluma", "tractocamion", "palacio", "bocina", "pan",
         "Libro", "Cigarro", "examen", "tarea", "software", "dado",
         "lentes", "lupa", "Mostaza", "Anciano", "Pensiones", "Valle",
         "Charco", "Monedero", "Plano", "Papel", "Botella", "Maceta",
         "Cuaderno", "Cuchillo", "Pantalones",
         "Chamarra", "Guitarra", "Flauta", "Librero", "Diamante", "Carreteras", "Antena", "Puente", "Sombrero",
         "Tijeras", "Helado", "Cama", "Cocina", "Abrigo", "Queso", "Calle",
         "Contrato", "Plato", "Azucar", "Mochila", "Barco", "Avión", "Escaleras",
         "Vestido", "Cobija", "Periódico", "Camisa", "Patineta", "oficina", "Refrigerador",
         "Cigarros", "Candado", "Perfume", "Botas", "Taladro", "Muelle", "cabaña",
         "microondas", "Graduado", "Concreto", "algas", "Balero", "Edificio", "Planos",
         "Chocolate", "Reloj", "mesabanco", "lámpara", "Foco", "Escoba",
         "Encendedor", "Frenos", "Paracaidas", "piel", "Barba", "Desierto",
         "Teatro", "Submarino", "Campana", "Crucero", "Farmacia", "Banco",
         "Tren", "Prisión", "Chiste", "Canguro", "Cerveza", "Zoológico",
         "Diccionario", "Papa", "Frenos", "Semaforo", "Nube", "Diente", "Pozo",
         "Bomba", "Radio", "Caracol", "Trofeo", "Energia", "Isla", "Ventana",
         "Abogado", "Bandera", "Jazz", "opera", "Funeral", "Fantasma", "Iglesia",
         "Serpiente", "Robot", "Tienda", "Chicle", "Dinosaurio", "cactus",
         "Bikini", "Isla", "Volcan", "lagrimas", "noche", "Prejuicio",
         "Angulo", "Pijama", "Corcho", "Politico", "Menu", "jamon", "policia",
         "espinaca", "supercalifragilisticoespidalidoso", "Jardin", "Hogar"
         )
word = random.choice(WORDS)
word2 = random.choice(WORDS)
word3 = random.choice(WORDS)
word4 = random.choice(WORDS)
word5 = random.choice(WORDS)
word6 = random.choice(WORDS)

print (
    "La primer palabra aleatoria es: ",word
    )
print (
    "La segunda palabra aleatoria es: ",word2
    )
print (
    "La tercera palabra aleatoria es: ",word3
    )
print (
    "La cuarta palabra aleatoria es: ",word4
    )
print (
    "La quinta palabra aleatoria es: ",word5
    )
print (
    "La sexta palabra aleatoria es: ",word6
    )
input("\n\nPresiona cualquier tecla para salir")
