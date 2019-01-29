import sqlite3
from Demo import stocks_dict

with sqlite3.connect('Trade') as db:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS TRADE(COMAPNAY_NAME TEXT, TOP1_DATE DATE, 
        TOP1_CLOSE FLOAT,TOP2_DATE DATE,TOP2_CLOSE FLOAT,PROFIT BOOLEAN)''')

    db_insert_data = list()
    for key, value in stocks_dict.iteritems():
        insertion_tuple = (value.get('company_name'),
                           value.get('top_1').get('date'),
                           value.get('top_1').get('close'),
                           value.get('top_2').get('date'),
                           value.get('top_2').get('close'),
                           value.get('profit'))
        db_insert_data.append(insertion_tuple)
    print db_insert_data
    sql1 = '''INSERT INTO TRADE VALUES(?,?,?,?,?,?)'''
    cursor.executemany(sql1, db_insert_data)
