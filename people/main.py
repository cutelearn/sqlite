import sqlite3
import csv
# import matplotlib.pyplot as plt
try:
    conn = sqlite3.connect("populations.db")    # 資料庫連線
    sql = '''Create table populationT(
            City TEXT,
            Lat int,
            Long int,
            City_Chinese text,
            Population int,
            Area text)'''
    conn.execute(sql)
except Exception as error:
    print(error)

fn = 'people/population.taiwan.csv'

with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)

    for row in listCsv:
        City = row[0]
        Lat = float(row[1])
        Long = float(row[2])
        City_Chinese = row[3]
        Population = int(row[4])
        Area = float(row[5])
        x = (City, Lat, Long, City_Chinese, Population, Area)
        sql = '''insert into populationT values(?,?,?,?,?,?)'''
        conn.execute(sql,x)
        conn.commit()

results = conn.execute("SELECT * from populationT")
for record in results:
    print("地區 =  ", record[0])
    print("緯度 = ", record[1])
    print("經度 = ", record[2])
    print("中文地區 = ", record[3])
    print("人頭數 = ", record[4])
    print("土地面積 = ", record[5])

conn.close()