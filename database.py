import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from datetime import date
from datetime import datetime


def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="online_auction")
    c = _conn.cursor()

    return c, _conn


def login_action(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from seller_details where email='" + username+"' and password='"+password+"'")
        print("--------SQL------")
        print(j)
        data=c.fetchall()
        for a in data:
            session['id'] = a[0]
            session['email_id'] = a[2]
            session['fname'] = a[1]
            session['mobile'] = a[3]
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def blogin_action(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from bidder_details where email='" + username+"' and password='"+password+"'")
        print("--------SQL------")
        print(j)
        data=c.fetchall()
        print(data)
        for a in data:
            session['id'] = a[0]
            session['email_id'] = a[2]
            session['fname'] = a[1]
            session['mobile'] = a[3]
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def alogin_action(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin_details where username='" + username+"' and password='"+password+"'")
        print("--------SQL------")
        print(j)
        data=c.fetchall()
        print(data)
        for a in data:
            session['email_id'] = 'admin'
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def bidderRegistration(fname, mobile, email, password):
    try:
        c, conn = db_connect()
        print(fname,mobile,email,password)
        j = c.execute("INSERT INTO `bidder_details`(`fname`, `email`, `mobile`, `password`) VALUES ('"+fname+"','"+email+"','"+mobile+"','"+password+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def sellerRegistration(fname, mobile, email, password):
    try:
        c, conn = db_connect()
        print(fname,mobile,email,password)
        j = c.execute("INSERT INTO `seller_details`(`fname`, `email`, `mobile`, `password`) VALUES ('"+fname+"','"+email+"','"+mobile+"','"+password+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def upload_product_action(category, p_name, specification, base_price, bid_sdate_time,bid_ldate_time, file_name):
    c, conn = db_connect()
    email=session['email']
    print(email)
    j = c.execute("INSERT INTO `product_details`(`category`, `p_name`, `specification`, `file_name`, `base_price`, `bid_sdate_time`, `bid_ldate_time`, `upload_by`) VALUES ('"+category+"','"+p_name+"','"+specification+"','"+file_name+"','"+base_price+"','"+bid_sdate_time+"','"+bid_ldate_time+"','"+file_name+"','"+email+"')")
    conn.commit()
    conn.close()
    return j


def seller_view_products():
    c,conn = db_connect()
    email=session['email']
    print(email)
    c.execute("SELECT * FROM `product_details` WHERE upload_by='"+email+"'")
    result = c.fetchall()
    conn.close()
    #print("result")
    return result

def viewBidders():
    c,conn = db_connect()
    c.execute("SELECT * FROM `bidder_details`")
    result = c.fetchall()
    conn.close()
    return result

def view_Sellers():
    c,conn = db_connect()
    c.execute("SELECT * FROM `seller_details`")
    result = c.fetchall()
    conn.close()
    return result

def biddingProduct(p_id):
    c,conn = db_connect()
    print(p_id)
    c.execute("SELECT * FROM `product_details` WHERE id='"+p_id+"'")
    result = c.fetchall()
    conn.close()
    return result

def biddingRequest(p_id):
    c,conn = db_connect()
    c.execute("SELECT * FROM `bidding_request` WHERE p_id='"+p_id+"'")
    result = c.fetchall()
    conn.close()
    return result


def bidder_view_products():
    c,conn = db_connect()
    email=session['email']
    print(email)
    c.execute("SELECT * FROM `product_details`")
    result = c.fetchall()
    conn.close()
    #print("result")
    return result


def seller_delete_product_action(id):
    c, conn = db_connect()
    j = c.execute("DELETE FROM `product_details` WHERE id='"+id+"'")
    conn.commit()
    conn.close()
    print("-----------delete Product-----------")
    print(j)
    return j

def bidder_delete_cart_product_action(id):
    c, conn = db_connect()
    j = c.execute("DELETE FROM `cart_whish_list_products` WHERE id='"+id+"'")
    conn.commit()
    conn.close()
    print("-----------delete Cart Product-----------")
    print(j)
    return j


def bidder_add_c(id):
    c, conn = db_connect()
    email=session['email']
    j = c.execute("INSERT INTO `cart_whish_list_products`(`p_id`, `request_by`,`status`) VALUES ('"+id+"','"+email+"','Wish List Product')")
    conn.commit()
    conn.close()
    print("----------- Product add in Cart-----------")
    print(j)
    return j

def bidderViewCartProducts():
    c,conn = db_connect()
    email=session['email']
    print(email)
    c.execute("SELECT t1.id, t1.p_id, t1.status, t2.* FROM cart_whish_list_products t1 INNER JOIN product_details t2 ON t1.p_id = t2.id  WHERE request_by='"+email+"'")
    result = c.fetchall()
    conn.close()
    return result