import csv

from flight_planner import app

def import_cities_from_csv(file_path, store):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            store.add_city(row['id'], {'name': row['name']})

    from flight_planner.csv_importer import import_cities_from_csv
    import_cities_from_csv('cities.csv', app.config['DATA_STORE'])