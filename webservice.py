
import json
from flask import  request, abort, Response,Flask
from db_functions import add_transaction_entry, spendPoints_calc, total_PlayerPoints, initialize, connect_sql

app = Flask(__name__)

#Route for adding transaction
@app.route("/api/addTransaction", methods=['POST'])
def insert_newTransaction():
    '''ADD TRANSACTION'''
    try:
        resp = request.json
        payer = str(resp['payer'])
        points = int(resp['points'])
        timestamp = str(resp['timestamp'])
    except:
        abort(400, 'Invalid Parameters')
    add_transaction_entry(sql,payer, points, timestamp)
    ret={"payer":payer,"points":points,"timestamp":timestamp}
    return Response('Added-:"'+json.dumps(ret), status=201)
   
        
#Route for spending points
@app.route("/api/spendPoints", methods=['POST'])
def spend_points():
    '''SPEND POINTS'''
    try:
        resp = request.json
        points = int(resp['points'])
    except:
        abort(400, 'Invalid Parameters')
    retValue = spendPoints_calc(sql,points)
    return retValue


#Route for all player point balance
@app.route("/api/totalPoints", methods=['GET'])
def total_player_balance():
    '''TOTAL POINTS OF EACH PLAYER'''
    total = total_PlayerPoints(sql)
    return json.dumps(total)


if __name__ == '__main__':
    #Create and intitalize DB and run the webservice
    sql=connect_sql()
    initialize(sql)
    # app.debug = True
    app.run(host='0.0.0.0', port='5000')