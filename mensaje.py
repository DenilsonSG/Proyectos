import requests
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, MI_NUMERO, WEATHER_API_KEY, CITY, COUNTRY_CODE

def obtener_clima():
    url = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}&aqi=no'
    response = requests.get(url)
    clima = response.json()
    return clima

def enviar_mensaje_twilio(mensaje):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=mensaje,
        from_=TWILIO_PHONE_NUMBER,
        to=MI_NUMERO
    )
    print(f'Mensaje enviado con ID: {message.sid}')

if __name__ == "__main__":
    clima = obtener_clima()

    if 'current' in clima:
        temperatura = clima['current']['temp_c']
        descripcion = clima['current']['condition']['text']
        mensaje = f'El clima en {CITY} es {descripcion} con una temperatura de {temperatura}°C.'
        enviar_mensaje_twilio(mensaje)
    else:
        print("La respuesta de la API no tiene la estructura esperada. Respuesta:", clima)
