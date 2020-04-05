import pymongo, csv, re

def read_data(csv_file, db):
    
    with open(csv_file, encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        artists_list = list(reader)
        keys = artists_list.pop(0)
        events = []
        for artist in artists_list:
            d = dict(zip(keys, artist))
            d['Цена'] = int(d['Цена'])
            events.append(d)
        client = pymongo.MongoClient()
        e_db = client[db]
        e_collection = e_db['events']
        e_collection.insert_many(events)

def find_cheapest(db):
    client = pymongo.MongoClient()
    e_db = client[db]
    e_collection = e_db['events']
    res = []
    for e in e_collection.find().sort('Цена', pymongo.ASCENDING):
        res.append(e)
    return res

def find_by_name(name, db):
    pattern = re.compile(name, re.IGNORECASE)
    client = pymongo.MongoClient()
    e_db = client[db]
    e_collection = e_db['events']
    res = []
    for e in e_collection.find({'Исполнитель': pattern}).sort('Цена', pymongo.ASCENDING):
        res.append(e)
    return res

if __name__ == '__main__':
    pass
    
