#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3


def characters(db):
    db.execute('''
        CREATE TABLE Character (
            id INTEGER,
            name VARCHAR(20),
            vel_ground REAL,
            vel_water REAL,
            vel_air REAL,
            vel_anti_gravity REAL,
            acc REAL,
            weight REAL,
            handle_ground REAL,
            handle_water REAL,
            handle_air REAL,
            handle_anti_gravity REAL,
            grip REAL,
            mini_turbo REAL);
            ''')

    records = [
        (0, 'mario', 3.75, 4.00, 4.25, 3.50, 3.50, 3.50, 3.50, 3.00, 3.50, 3.50, 3.50, 3.25),
        (1, 'luigi', 3.75, 4.00, 4.25, 3.50, 3.50, 3.50, 3.75, 3.25, 3.75, 3.75, 3.25, 3.25),
        ]

    sql = 'INSERT INTO Character VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    db.executemany(sql, records)


def karts(db):
    db.execute('''
        CREATE TABLE Kart (
            id INTEGER,
            name VARCHAR(20),
            vel_ground REAL,
            vel_water REAL,
            vel_air REAL,
            vel_anti_gravity REAL,
            acc REAL,
            weight REAL,
            handle_ground REAL,
            handle_water REAL,
            handle_air REAL,
            handle_anti_gravity REAL,
            grip REAL,
            mini_turbo REAL,
            is_hung BOOL);
            ''')

    records = [
        (0, 'standard_kart', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False),
        (1, 'pip_frame', -0.5, 0, -0.5, -0.5, 0.5, -0.25, 0.5, 0.5, -0.25, 0.25, 0.25, 0.5, False),
        ]

    sql = 'INSERT INTO Kart VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    db.executemany(sql, records)


def tires(db):
    db.execute('''
        CREATE TABLE Tire (
            id INTEGER,
            name VARCHAR(20),
            vel_ground REAL,
            vel_water REAL,
            vel_air REAL,
            vel_anti_gravity REAL,
            acc REAL,
            weight REAL,
            handle_ground REAL,
            handle_water REAL,
            handle_air REAL,
            handle_anti_gravity REAL,
            grip REAL,
            mini_turbo REAL);
            ''')

    records = [
        (0, 'standard', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 'monster', 0, -0.25, -0.5, 0, -0.5, 0.5, -0.75, -0.5, -0.5, -0.75, 0.5, -0.25),
        ]

    sql = 'INSERT INTO Tire VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    db.executemany(sql, records)


def gliders(db):
    db.execute('''
        CREATE TABLE Glider (
            id INTEGER,
            name VARCHAR(20),
            vel_ground REAL,
            vel_water REAL,
            vel_air REAL,
            vel_anti_gravity REAL,
            acc REAL,
            weight REAL,
            handle_ground REAL,
            handle_water REAL,
            handle_air REAL,
            handle_anti_gravity REAL,
            grip REAL,
            mini_turbo REAL);
            ''')

    records = [
        (0, 'standard', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 'cloud_glider', -0.25, 0, 0.25, 0.25, 0.25, -0.25, 0, 0, 0.25, 0, 0, 0.25),
        ]

    sql = 'INSERT INTO Glider VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    db.executemany(sql, records)


if __name__ == '__main__':
    os.remove('mk8dx.db')

    db = sqlite3.connect(
        'mk8dx.db',
        isolation_level=None,)

    characters(db)
    karts(db)
    tires(db)
    gliders(db)

    db.close()
