import json
import sqlite3
from datetime import datetime

commands={ "table":""" CREATE TABLE IF NOT EXISTS TransactionRecord(
            payer VARCHAR(255) NOT NULL,
            points INT NOT NULL,
            timestamp TEXT NOT NULL
        ); """,
        "selectALL":"""SELECT * FROM TransactionRecord""",
        "insert":"""INSERT INTO TransactionRecord VALUES (?,?,?)""",
        "spend":"""SELECT payer, points FROM TransactionRecord ORDER BY timestamp ASC""",
        "total":"""SELECT payer, sum (points), MIN(timestamp) FROM TransactionRecord GROUP BY payer ORDER BY timestamp ASC"""
}

def connect_sql():
    '''Connects to an SQLite DB and return connection variable'''

    sqlConnect = sqlite3.connect('sql.db',check_same_thread=False)
    return sqlConnect

def initialize(sqlConnect):
    '''Takes in a DB as input and creates table TransactionRecord in the DB'''

    #use command "table" from commands and create the table
    cursor = sqlConnect.cursor()
    table = commands["table"]
    cursor.execute(table)
    sqlConnect.commit()
    cursor.close()

def display_allData(sqlConnect):
    '''Takes in a DB as input and prints all data in the table TransactionRecord'''

    #use command "selectAll" from commands and display all entries
    cursor = sqlConnect.cursor()
    cursor.execute(commands["selectALL"])
    for row in cursor:
        print(row)
    cursor.close()
    
def add_transaction_entry(sqlConnect,payer, points, timestamp):
    '''Takes in DB, payer, points and timestamp as input and adds new transaction to table TransactionRecord'''

    #use command "insert" from commands and add new entry
    cursor = sqlConnect.cursor()
    record = (payer, points, timestamp)
    cursor.execute(commands["insert"], record)
    cursor.close()

def spendPoints_calc(sqlConnect,totalPoints):
    '''Takes in DB and totalpoints to deduct as input and performs required transactions and adds those transaction to table TransactionRecord'''
    
    #use command "spend" from commands and get all entries arranged by timestamp
    cursor = sqlConnect.cursor()
    dictOfPlayer = {}
    cursor.execute(commands["spend"])
    
    #loop through each entry and deduct points
    for row in cursor:
        
        payer, points = row
        #New payer initialization
        if payer not in dictOfPlayer:
            dictOfPlayer[payer] = 0
        
        #Total points still left
        if totalPoints > points:
            
            dictOfPlayer[payer] -= points
            totalPoints -= points
        else:
            dictOfPlayer[payer] -= totalPoints
            break
    #Add new entries of deduction to the table with current timestamp and return the record of deduction in a list
    cursor.close()
    returnList=[]
    #Loop through dictionary of deducations
    for i,j in dictOfPlayer.items():
        #Get current time and format it to match entry format
        currTime = datetime.now()
        formatTime = currTime.strftime("%Y-%d-%mT%H:%M:%SZ")
        #Add transaction to table
        add_transaction_entry(sqlConnect,i,j,formatTime)
        #Format output in the way we want
        temp={}
        temp["payer"]=i
        temp["points"]=j
        returnList.append(temp)
    return returnList

def total_PlayerPoints(sqlConnect):
    '''Takes in DB as input and returns total points of each user'''
    
    #use command "total" from commands and get total points of each player
    cursor = sqlConnect.cursor()
    total = {}
    cursor.execute(commands["total"])
    #Loop through each entry and add it into our return dict
    for row in cursor:
        payer, points, date = row
        total[payer]=points
    cursor.close()
    return (total)

# l1={ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
# l2={ "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }
# l3={ "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" }
# l4={ "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }
# l5={ "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
# l2={ "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }
# l4={ "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }
# l5={ "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
# sqlConnect=connect_sql()
# initialize(sqlConnect)
# # add_transaction_entry(sqlConnect,l1["payer"],l1["points"],l1["timestamp"])
# add_transaction_entry(sqlConnect,l2["payer"],l2["points"],l2["timestamp"])
# # add_transaction_entry(sqlConnect,l3["payer"],l3["points"],l3["timestamp"])
# add_transaction_entry(sqlConnect,l4["payer"],l4["points"],l4["timestamp"])
# add_transaction_entry(sqlConnect,l5["payer"],l5["points"],l5["timestamp"])

# # show_db(sqlConnect)
# print(spendPoints_calc(sqlConnect,5000))
# # show_db(sqlConnect)
# print(total_PlayerPoints(sqlConnect))