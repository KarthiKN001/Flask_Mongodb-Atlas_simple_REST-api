import pymongo

link = "< ********* Here you need to paste the link of Mongodb Atlas for connect with application ************ >"


client = pymongo.MongoClient(link)
mydb = client["Joker"]                  # your database name
coll = mydb["demo"]                # your collection name
                                          

def add_item(name, price, quantity):
    new_stock = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    coll.insert_one(new_stock)


def get_items():
    a = []
    for i in coll.find():
        a.append(i['name'])

    return a


def get_item_info(name):
    b = coll.find_one({'name':name})
    return b


def update_stock(name, price, quantity):
    for i in coll.find():
        if i['name'] == name:
            need_update = {
                'price': price,
                'quantity': quantity
            }
            item_fix = {'name': name}
            new_stock = {'$set': need_update}

            coll.update_one(item_fix, new_stock)


def delete_item(name):
    coll.delete_one({'name':name})

