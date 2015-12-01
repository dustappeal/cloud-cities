import csv

# columns from http://openflights.org/data.html
columns = ["Airport ID", "Name", "City", "Country", "IATA/FAA", "ICAO",
        "Latitude", "Longitude", "Altitude", " Timezone", "DST",
        "Tz database time zone"]

def read(filename):
    airports = {}
    population = 0
    skipped = 0
    with open(filename, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        last_read = None
        try: 
            for row in reader:
                airport = [row[4], row[2], row[3], row[6], row[7]]
                last_read = airport
                if len(airport[4]) > 0:
                    airports[airport[0]] = airport
                else:
                    skipped += 1
        except Exception as exc:
            print "Failed to read the airport after" + last_read
        finally:
            print "Read %d airports and skipped %d " % (len(airports), skipped)
    return airports

