import random

palabras = ("Boleto", "Sidra", "Sueño", "Dragón", "Carro",  "Lavamanos", "Colador", "Cine", "Gladiador",
            "Computadora", "Celular", "Lapiz", "Pluma", "Tractocamion", "Palacio", "bocina", "pan",
            "Libro", "Cigarro", "Examen", "tarea", "software", "dado",
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

lista = random.sample(palabras, 6)

print("\nTus palabras son: {}, {}, {}, {}, {} y {}".format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5]))