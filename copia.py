import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("El api key no se encuentra en .env")
    exit()

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.7-flash"
)

print("Chat inciado")
print("Para terminar la sesion escribir 'salir'")

while True:
    pregunta = input("Tu: ")

    if pregunta.strip().lower() == "salir":
        break

    try:
        respuesta = chat.send_message(
            message=pregunta
        )
        print(f"IA: {respuesta.text}")
    except Exception as error:
        print(f"Ocurrion un error: {error}")

print("Programa finalizado")