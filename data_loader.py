"""Утиліти для завантаження даних з файлів"""

import csv
import random
import re

CSV_GOOGLE_PLAY_STORE = "data/googleplaystore.csv"
CSV_UBER = "data/uber.csv"


def to_bytes(value, unit_of_measure):
    """Функція для приведення даних до однієї одиниці виміру"""
    multiplicator = 1
    if unit_of_measure == "K":
        multiplicator = 1024
    if unit_of_measure == "M":
        multiplicator = 1024 * 1024
    return float(value) * multiplicator


def get_google_play_data():
    """Завантаження та очищення набору даних з розмірами застосунків з Google Play Store"""
    # Завантажуємо дані з CSV
    data = []
    with open(CSV_GOOGLE_PLAY_STORE, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            data.append(row[4])

    # Очищаємо дані від некоретних та приводимо до однієї одиниці виміру
    clean_data = []
    for e in data:
        m = re.match(r"(\d+\.?\d+)(M?K?)", e.upper())
        if m is not None:
            value = m.group(1)
            unit_of_measure = m.group(2)
            clean_data.append(to_bytes(value, unit_of_measure))

    return clean_data


def get_uber_data():
    """Завантаження та очищення набору даних з вартістю поїздок Uber"""
    # Завантажуємо дані з CSV
    data = []
    with open(CSV_UBER, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            data.append(row[2])

    # Очищаємо дані від некоретних
    clean_data = []
    for e in data:
        m = re.match(r"(-?\d+\.?\d+)", e.upper())
        if m is not None:
            value = m.group(1)
            clean_data.append(float(value))
        # На час відладки
        if len(clean_data) > 200000:
            return clean_data

    return clean_data


def get_random_data(number_of_elements):
    """Формування випадкового набору даних"""
    # Завантажуємо дані з CSV
    data = []
    random.seed(42)

    for i in range(number_of_elements):
        data.append(random.randint(0, number_of_elements * 3))

    return data
