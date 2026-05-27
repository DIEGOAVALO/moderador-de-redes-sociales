# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "¡Excelente contenido! Me sirvió muchísimo para mi tarea.",          # Seguro
    "Este usuario es un bobo, no le hagan caso.",                        # Tóxico (bobo)
    "¿Alguien sabe a qué hora empieza la transmisión en vivo?",          # Seguro
    "Qué video tan estúpido, perdiste un seguidor.",                     # Tóxico (estúpido)
    "Muchas gracias por la explicación, quedó todo muy claro.",         # Seguro
    "No me gustó mucho el ritmo del video, pero la info es buena.",      # Seguro (Crítica constructiva)
    "El peor canal de la plataforma, eres un tonto.",                    # Tóxico (tonto)
    "¿Podrías hacer un tutorial sobre cómo usar bases de datos?",        # Seguro
    "Vete al diablo con tus opiniones políticas.",                       # Tóxico (diablo)
    "Un saludo desde México, sigan así con el proyecto."                 # Seguro
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)
palabras_toxicas = ["tonto", "diablo", "bobo", "estúpido"]

def modelo_ia_moderador(comentario):
    # Convertimos a minúsculas para evitar evadir el filtro con Mayúsculas
    comentario_minuscula = comentario.lower()
    
    # El modelo busca si hay lenguaje ofensivo
    for palabra in palabras_toxicas:
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)" # Predicción 1
            
    return "APROBADO (Seguro)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- MODERADOR DE REDES SOCIALES ---")
for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
