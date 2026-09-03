import os
from dotenv import load_dotenv
from google import genai

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la API key
api_key = os.getenv("GEMINI_API_KEY")

# Comprobar que exista la API key
if not api_key:
    print("Error: no se encontró GEMINI_API_KEY en el archivo .env")
    exit()

# Crear cliente de Gemini
client = genai.Client(api_key=api_key)

# Crear una conversación
chat = client.chats.create(
    model="gemini-3.7-flash"
)

print("Chat iniciado.")
print("Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("Tú: ")

    if pregunta.strip().lower() == "salir":
        break

    try:
        respuesta = chat.send_message(
            message=pregunta
        )

        print(f"\nIA: {respuesta.text}\n")

    except Exception as error:
        print(f"\nOcurrió un error: {error}\n")

print("Programa finalizado.")