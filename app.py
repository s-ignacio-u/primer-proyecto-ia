import os
from dotenv import load_dotenv
from google import genai

# Cargar las variables guardadas en .env
load_dotenv()

# Obtener nuestra clave secreta
api_key = os.getenv("GEMINI_API_KEY")

# Crear el cliente para comunicarnos con Gemini
client = genai.Client(api_key=api_key)

# Pedirle una pregunta al usuario
pregunta = input("Escribe tu pregunta: ")

# Enviar la pregunta a Gemini
respuesta = client.interactions.create(
    model="gemini-3.6-flash",
    input=pregunta
)

# Mostrar la respuesta
print("\nRespuesta:\n")
print(respuesta.output_text)