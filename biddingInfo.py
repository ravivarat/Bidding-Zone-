import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import date
from datetime import datetime
from database import biddingDetails,db_connect

def biddingDetails(p_id):
    try:
        c, conn = db_connect()
        email=session['email']
        j = c.execute("select * from bidding_request where p_id='" + p_id+"' and request_by='"+email+"'")
        print("--------SQL------")
        print(j)
        data=c.fetchall()
        conn.close()
        return data
    except Exception as e:
        return(str(e))

