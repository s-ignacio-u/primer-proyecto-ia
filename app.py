import os
from dotenv import load_dotenv
from google import genai

# Cargar las variables guardadas en .env
load_dotenv()

# Obtener nuestra clave secreta
api_key = os.getenv("GEMINI_API_KEY")

# Crear el cliente para comunicarnos con Gemini
client = genai.Client(api_key=api_key)

historial = []

while True:
    # Pedir una pregunta al usuario
    pregunta = input("\nEscribe tu pregunta: ")
    
    # Finalizar el programa
    if pregunta.strip().lower() == "salir":
        break
    
    historial.append(f"Usuario: {pregunta}")

    contexto = "\n".join(historial)
    # Enviar la pregunta a Gemini
    respuesta = client.interactions.create(
        model="gemini-3.6-flash",
        input=contexto
    )

    historial.append(f"IA: {respuesta.output_text}")

    # Mostrar la respuesta
    print("\nRespuesta:\n")
    print(respuesta.output_text)

print("\nPrograma finalizado.")