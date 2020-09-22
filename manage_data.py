#!/usr/local/bin/python
# coding: utf-8

import os
import pandas as pd
import pandas.io.sql as sql
from openpyxl import load_workbook
from itertools import islice
import sqlite3
import django
django.setup()
from collisions.models import Violations_cameras, Dtp, Test
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rti_project.settings")


# создаем список двоичных файлов в каталоге /data/csv/ с постфиксом *_pickle.csv
def create_list_pickle_csv():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory_csv = current_directory + '/data/csv'
    list_files_csv = os.listdir(directory_csv)
    list_files_pickle_csv = []
    for file in list_files_csv:
        words = file.rsplit('.')[0].split('_')
        if 'pickle' in words:
            list_files_pickle_csv.append(file)
    return list_files_pickle_csv


def read_pickle_csv(file_name):
    directory = os.path.dirname(os.path.abspath(__file__))
    address = str(directory) + '/data/csv/' + file_name
    frame = pd.read_pickle(address)
    return frame


# читаем файл /data/csv/*.csv и пересохраняем его в том же каталоге в двоичном формате /data/csv/*_pickle.csv
def csv_to_pickle(file_name):
    year = file_name.split('.')[0]
    directory = os.path.dirname(os.path.abspath(__file__))
    address = str(directory) + '/data/csv/' + file_name
    frame = pd.read_table(address, sep=';', parse_dates=True, dayfirst=True, nrows=10, encoding='UTF-8')
    frame.drop('Unnamed: 0', axis=1)
    frame['year'] = year
    frame2 = frame.set_index(['Unnamed: 0'])
    print(frame2)
    frame2.to_pickle('./data/csv/' + str(year) + '_pickle.csv')


# переводим все файлы в каталоге /data/csv/ с расширением .csv в файлы в двоичном формате с постфиксом _pickle.csv
# этим достигается сжатие исходных файлов приблизтельно в 2,3 раза
def all_csv_to_pickle():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directory_csv = current_directory + '/data/csv'
    list_files_csv = os.listdir(directory_csv)
    list_files_no_pickle_csv = []
    for file in list_files_csv:
        words = file.rsplit('.')[0].split('_')
        if 'pickle' not in words:
            list_files_no_pickle_csv.append(file)
    for file in list_files_no_pickle_csv:
       csv_to_pickle(file)


def csv_to_table_violations_cameras(file_name):
    year = file_name.split('.')[0]
    # directory = os.path.dirname(os.path.abspath(__file__))
    address = '/home/aypa/projects/dtp-stat/data/csv/' + file_name
    # address = str(directory) + '/data/csv/' + file_name
    with open(address) as f:
        my_list = [line.split(';') for line in f]
    for line in my_list[1:]:
        line.pop(0)
        line.insert(0, year)
        speed = line[-1].strip('\n')
        line[-1] = speed
        correct_point_8 = format_coordinates(line[8])
        line[8] = correct_point_8
        correct_point_9 = format_coordinates(line[9])
        line[9] = correct_point_9
        # print(line)
        insert_to_table_violations_cameras(line)


def format_coordinates(point):
    point.replace(' ', '')
    if len(point) == 9:
        pass
    if len(point) < 9:
        zero_position = 9 - len(point)
        point = point + '0'*zero_position
    if len(point) > 9:
        point = point[0:9]
    return point


def insert_to_table_violations_cameras(data_list):
    violation = Violations_cameras(
        year=str(data_list[0]),
        id_violations=str(data_list[1]),
        date=str(data_list[2]),
        time=str(data_list[3]),
        date_time=str(data_list[4]),
        id_cameras=str(data_list[5]),
        model_cameras=str(data_list[6]),
        type_cameras=str(data_list[7]),
        latitude=str(data_list[8]),
        longitude=str(data_list[9]),
        article_offenses_in_CODE=str(data_list[10]),
        content_article=str(data_list[11]),
        speed_of_violation=str(data_list[12]),
    )
    violation.save()


# def insert_to_table_violations_cameras(data_tuple):
#     data = [data_tuple]
#     stmt = "INSERT INTO collisions_violations_cameras VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#     con = sqlite3.connect('db.sqlite3')
#     con.executemany(stmt, data)
#     con.commit()


def read_table_violations_cameras():
    con = sqlite3.connect('db.sqlite3')
    frame = sql.read_sql('select * from collisions_violations_cameras', con)
    print(frame)


# переформатирование файла *.xlsx в *.csv
def xlsx_to_table_dtp(file_name):
    year = file_name.split('.')[0]
    directory = os.path.dirname(os.path.abspath(__file__))
    address = '/home/aypa/projects/dtp-stat/data/xlsx/' + file_name
    # address = str(directory) + '/data/xlsx/' + file_name
    wb = load_workbook(address)
    print(wb.get_sheet_names())
    first_sheet = wb.get_sheet_names()[0]
    sheet = wb.get_sheet_by_name(first_sheet)
    data = sheet.values
    cols = next(data)[1:]
    data = list(data)
    idx = [r[0] for r in data]
    data = (islice(r, 1, None) for r in data)
    frame = pd.DataFrame(data, index=idx, columns=cols)
    to_address = 'data/xlsx/' + year + '.csv'
    frame.to_csv(to_address, sep=';', index=False, na_rep='NULL')


def csv_to_table_dtp(file_name):
    year = file_name.split('.')[0]
    directory = os.path.dirname(os.path.abspath(__file__))
    address = '/home/aypa/projects/dtp-stat/data/xlsx/' + file_name
    # address = str(directory) + '/data/xlsx/' + file_name
    with open(address) as f:
        my_list = [line.split(';') for line in f]
    for line in my_list[1:]:
        line.insert(0, year)
        correct_point_51 = format_coordinates(line[51])
        line[51] = correct_point_51
        correct_point_52 = format_coordinates(line[52])
        line[52] = correct_point_52
        insert_to_table_dtp(line)


def insert_to_table_dtp(data_list):
    dtp = Dtp(
        year=str(data_list[0]),
        number_accident=str(data_list[1]),
        date=str(data_list[2]),
        time=str(data_list[3]),
        type_accident=str(data_list[4]),
        place=str(data_list[5]),
        street=str(data_list[6]),
        home=str(data_list[7]),
        road=str(data_list[8]),
        kilometer=str(data_list[9]),
        metre=str(data_list[10]),
        latitude_degrees=str(data_list[11]),
        latitude_minutes=str(data_list[12]),
        latitude_seconds=str(data_list[13]),
        longitude_degrees=str(data_list[14]),
        longitude_minutes=str(data_list[15]),
        longitude_seconds=str(data_list[16]),
        lost=str(data_list[17]),
        lost_children=str(data_list[18]),
        wounded=str(data_list[19]),
        wounded_children=str(data_list[20]),
        division_reg_accident=str(data_list[21]),
        ndu=str(data_list[22]),
        ndu_1=str(data_list[23]),
        ndu_2=str(data_list[24]),
        ndu_3=str(data_list[25]),
        uds_objects_in_place=str(data_list[26]),
        uds_objects_in_place_1=str(data_list[27]),
        uds_objects_nearby=str(data_list[28]),
        uds_objects_nearby_1=str(data_list[29]),
        uds_objects_nearby_2=str(data_list[30]),
        uds_objects_nearby_3=str(data_list[31]),
        factors_of_driving_mode=str(data_list[32]),
        factors_of_driving_mode_1=str(data_list[33]),
        factors_of_driving_mode_2=str(data_list[34]),
        factors_of_driving_mode_3=str(data_list[35]),
        condition_of_carriageway=str(data_list[36]),
        weather_condition=str(data_list[37]),
        weather_condition_1=str(data_list[38]),
        lighting=str(data_list[39]),
        concentration_accidents=str(data_list[40]),
        road_on_plan=str(data_list[41]),
        profile_of_road=str(data_list[42]),
        number_of_lanes=str(data_list[43]),
        lane_where_accident=str(data_list[44]),
        width_roadway=str(data_list[45]),
        width_shoulder=str(data_list[46]),
        width_sidewalk=str(data_list[47]),
        width_dividing_strip=str(data_list[48]),
        type_dividing_strip=str(data_list[49]),
        type=str(data_list[50]),
        latitude=str(data_list[51]),
        longitude=str(data_list[52]),
        location=str(data_list[53])
    )
    dtp.save()


# def insert_to_table_dtp(data_tuple):
#     data = [data_tuple]
#     stmt = "INSERT INTO collisions_dtp VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#     con = sqlite3.connect('db.sqlite3')
#     con.executemany(stmt, data)
#     con.commit()


def insert_to_test():
    test = Test(
        first_name='yury',
        last_name='bor',
    )
    test.save()


if __name__ == "__main__":
    # all_csv_to_pickle()
    # insert_to_table_violations_cameras('2018.csv')
    # insert_to_table_dtp('2017.csv')
    # csv_to_table_dtp('2019.csv')
    # csv_to_table_violations_cameras('2020.csv')
    insert_to_test()

