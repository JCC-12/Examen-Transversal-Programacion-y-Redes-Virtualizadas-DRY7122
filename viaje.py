import geopy.distance
import requests

def obtener_coordenadas(ciudad):
    # Aquí utilizamos una API gratuita para obtener las coordenadas de la ciudad
    # Nota: Es posible que necesites una clave API para servicios de geocodificación como OpenCage, MapQuest, etc.
    response = requests.get(f"https://nominatim.openstreetmap.org/search?q={ciudad}&format=json")
    if response.status_code == 200 and len(response.json()) > 0:
        return float(response.json()[0]['lat']), float(response.json()[0]['lon'])
    else:
        print(f"No se pudieron obtener las coordenadas para {ciudad}.")
        return None

def calcular_distancia(ciudad_origen, ciudad_destino):
    coords_origen = obtener_coordenadas(ciudad_origen)
    coords_destino = obtener_coordenadas(ciudad_destino)
    if coords_origen and coords_destino:
        return geopy.distance.distance(coords_origen, coords_destino).km
    else:
        return None

def calcular_duracion(distancia, medio_transporte):
    velocidades = {
        "auto": 80,   # km/h
        "bus": 60,    # km/h
        "tren": 100,  # km/h
        "avion": 800  # km/h
    }
    if medio_transporte in velocidades:
        return distancia / velocidades[medio_transporte]
    else:
        print("Medio de transporte no válido.")
        return None

def main():
    while True:
        origen = input("Ingrese la Ciudad de Origen (o 'e' para salir): ")
        if origen.lower() == 'e':
            break
        destino = input("Ingrese la Ciudad de Destino: ")
        medio_transporte = input("Ingrese el medio de transporte (auto, bus, tren, avion): ").lower()
        
        distancia_km = calcular_distancia(origen, destino)
        if distancia_km:
            distancia_millas = distancia_km * 0.621371
            duracion_horas = calcular_duracion(distancia_km, medio_transporte)
            
            if duracion_horas:
                print(f"Distancia entre {origen} y {destino}:")
                print(f"- En kilómetros: {distancia_km:.2f} km")
                print(f"- En millas: {distancia_millas:.2f} millas")
                print(f"Duración del viaje en {medio_transporte}: {duracion_horas:.2f} horas")
                print(f"Narrativa del viaje: Viajar de {origen} a {destino} en {medio_transporte} tomará aproximadamente {duracion_horas:.2f} horas cubriendo una distancia de {distancia_km:.2f} kilómetros.")

if __name__ == "__main__":
    main()
