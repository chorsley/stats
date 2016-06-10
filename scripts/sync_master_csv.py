import urllib

riskscsv = 'https://docs.google.com/spreadsheets/d/1PosJEjJ-exlPER8ycVwWtDdQOuCsj-41Ctiuts7qGVY/pub?gid=0&single=true&output=csv'
risksfp = 'content/data/risks.csv'
placescsv = 'https://docs.google.com/spreadsheets/d/1PosJEjJ-exlPER8ycVwWtDdQOuCsj-41Ctiuts7qGVY/pub?gid=1500421369&single=true&output=csv'
placesfp = 'content/data/places.csv'

urllib.urlretrieve(riskscsv, risksfp)
urllib.urlretrieve(placescsv, placesfp)

