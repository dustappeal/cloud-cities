# Reads the allCities file into a python in-memory data structure
import csv

columns = ["geonameid", "name", "asciiname", "alternatenames", "latitude",
        "longitude", "feature class", "feature code", "country code", "cc2",
        "admin1 code", "admin2 code", "admin3 code", "admin4 code",
        "population", "elevation", "dem", "timezone", "modification date"]

new_columns = ['name', 'lat', 'long', 'country', 'population']

def read_city(row):
    city = [row[2], row[4], row[5], row[8], row[14]]
    return city

def read(filename):
    cities = {}
    population = 0
    with open(filename, 'rb') as cities_file:
        reader = csv.reader(cities_file, delimiter='\t', quoting=csv.QUOTE_NONE)
        last_read = None
        try: 
            for row in reader:
                city = read_city(row)
                last_read = city
                cities[city[0]] = city
                population += int(city[4])
        except Exception as exc:
            print "Failed to read the city after" + last_read
        finally:
            print "Read %d cities with a total population of %d million people." % (len(cities),
                    population/1000000)
    return cities
