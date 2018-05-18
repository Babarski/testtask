import MySqlDb as MSD
import re

def getTables(date):
    tables = []
    mysql = MSD.MySqlDb()
    queryResultTables = mysql.getAllTables(date)
    for querytable in queryResultTables:
        if querytable[7] == None:
            reserved = 0
        else:
            reserved = 1

        elements=['seats', "form","coordLength","coordWidth","sizeLength","sizeWidth","reserved", "id"]
        table = {
            elements[7]: querytable[0],
            elements[0]: querytable[1],
            elements[1]: querytable[2],
            elements[2]: querytable[3],
            elements[3]: querytable[4],
            elements[4]: querytable[5],
            elements[5]: querytable[6],
            elements[6]: reserved,
        }
        tables.append(table)
    return tables

def isUserExists(login, password):
    mysql = MSD.MySqlDb()
    if mysql.getUser(login, password) == 1:
        return True
    else:
        return False

def setTable(seats, form, coordLength, coordWidth, sizeLength, sizeWidth):
    mysql = MSD.MySqlDb()
    mysql.setTable(seats, form, coordLength, coordWidth, sizeLength, sizeWidth)


def setOrder(name, email, date, tables):
    tables = tables.split(',')
    mysql = MSD.MySqlDb()
    for table in tables:
        tableSTR = table.encode('ascii')
        table_id = re.findall("\d+", tableSTR)
        mysql.setOrder(name, date, table_id[0])
