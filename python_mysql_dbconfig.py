from configparser import ConfigParser

#def mysql_db_config(filename="config.ini",section="mysql"):
def mysql_db_config(filename, section):
    parser=ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        db = {}
        db_items=parser.items(section)
        #print(db_items)
        for item_ind in db_items:
            db[item_ind[0]]=item_ind[1]
        #print(dict1)
    else:
        raise Exception("{1} is not found in {0}".format(filename,section))

    return db
