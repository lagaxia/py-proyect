import os
import utils
import read_csv
import charts

def get_population_ratio(datos):
  continent = input('What continent are you interested in? Write your answer: ')
  continent = continent.title()
  datos = list(filter(lambda item: item['Continent'] == continent, datos))
  print(continent)
  paises = [item['Country'] for item in datos]
  ratios = [float(item['World Population Percentage']) for item in datos]
  return paises, ratios

'''En esta función se usa list comprehensions. Se está recorriendo a DATOS, que es
una lista compuesta de diccionarios, y cada uno de estos se denomina ITEM. Luego,
cada uno de estos ITEM se le solicita el valor asociado a la clave COUNTRY/TERRITORY o WORLD POPULATION PERCENTAGE. Otra solución:
def get_world_percentages(data):
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}

    names = percentages_dict.keys()
    per = percentages_dict.values()

    return names, per'''
    
def run():
    # Ruta al archivo CSV
    csv_path = 'poblacion.csv'
    
    # Verificar que el archivo exista antes de leerlo
    if not os.path.exists(csv_path):
        print(f"Error: El archivo {csv_path} no existe.")
        return
    
    # Leer y filtrar datos
    data = read_csv.read_csv(csv_path)
    
    if not data:
        print("No se encontraron datos para Sudamérica.")
        return
    
    # Obtener nombres y porcentajes para el gráfico
    names, per = get_population_ratio(data)
    charts.generate_pie_chart(names, per)
    

if __name__ == '__main__':
    run()
    

#suma lambda
suma = lambda x,y: x+y
print(suma(2,2))