import os
import utils
import read_csv
import charts
import pandas as pd

'''En esta función se usa list comprehensions. Se está recorriendo a DATOS, que es
una lista compuesta de diccionarios, y cada uno de estos se denomina ITEM. Luego,
cada uno de estos ITEM se le solicita el valor asociado a la clave COUNTRY/TERRITORY o WORLD POPULATION PERCENTAGE. Otra solución:
def get_world_percentages(data):
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}

    names = percentages_dict.keys()
    per = percentages_dict.values()

    return names, per'''
#adentro de la funcion    
'''
# Verificar que el archivo exista antes de leerlo

    data = read_csv.read_csv('poblacion.csv')
    data = list(filter(lambda item : item['Continent'] == 'South America',data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
'''   
def run():
    df = pd.read_csv('poblacion.csv')
    df = df[df['Continent'] == 'Africa']
    
    countries = df['Country'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)
    
    data = read_csv.read_csv('poblacion.csv')
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'],labels, values)
  

if __name__ == '__main__':
    run()
    

