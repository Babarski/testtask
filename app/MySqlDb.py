import pymysql
import yaml

class MySqlDb(object):
    def __init__(self):
        with open("./app/configs/configs.yml", 'r') as ymlfile:
            conf = yaml.load(ymlfile)
            self.mysqlConfig = conf['mysql']

        self.conn = pymysql.connect(host=self.mysqlConfig['host'],
                                    port=self.mysqlConfig['port'],
                                    user=self.mysqlConfig['user'],
                                    #password=self.mysqlConfig['password'],
                                    db=self.mysqlConfig['db'])
        self.a = self.conn.cursor()
        self.dinnerTables = self.mysqlConfig['dinnerTables']
        self.orders = self.mysqlConfig['ordersTable']

    def getAllTables(self, date):

        getAllTables = 'SELECT * FROM `'+self.dinnerTables+'` LEFT JOIN `'+self.orders +'` ON `'+self.dinnerTables+'`.`id` = `'+self.orders +'`.`idDinnerTable` \
        AND `'+self.orders +'`.`date` ="'+date+'";'

        self.a.execute(getAllTables)
        allTables = self.a.fetchall()
        return allTables

    def getUser(self, login, password):
        getUser = 'SELECT * FROM `users` WHERE `users`.`login`="'+str(login)+'" AND `users`.`password`="'+str(password)+'"'
        user = self.a.execute(getUser)
        return user

    def setTable(self, seats, form, coordLength, coordWidth, sizeLength, sizeWidth):
        setTable = 'INSERT INTO `'+self.dinnerTables+'` (seats, form, coordinateLength, coordinateWidth, sizeLength, sizeWidth) \
                    VALUES ("'+seats+'","'+form+'", "'+coordLength+'","'+coordWidth+'","'+sizeLength+'","'+sizeWidth+'");'

        self.a.execute(setTable)
        self.conn.commit()

    def setOrder(self, name, date, table):
        setOrder = 'INSERT INTO `orders` (idDinnerTable, date, ordersName) VALUES ("'+table+'", "'+date+'", "'+name+'");'
        self.a.execute(setOrder)
        self.conn.commit()
