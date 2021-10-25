#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


def print_db(db, table_name):
    print(table_name)
    c = db.cursor()

    sql = f'SELECT * FROM {table_name}'

    c.execute(sql)

    for item in c:
        print(item)


if __name__ == '__main__':
    db = sqlite3.connect(
        'mk8dx.db',
        isolation_level=None)

    table_names = ['Character', 'Kart', 'Tire', 'Glider']

    [print_db(db, table_name) for table_name in table_names]

    db.close()
