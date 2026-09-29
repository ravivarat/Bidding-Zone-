import os
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect, login_action, sellerRegistration,upload_product_action,seller_delete_product_action,seller_view_products,blogin_action,bidderRegistration,bidder_view_products,bidder_add_c
from database import bidderViewCartProducts,bidder_delete_cart_product_action,biddingProduct,biddingRequest,alogin_action
from database import view_Sellers, viewBidders
#from biddinginfo import biddingDetails


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")
#<!-------------------------------------------------Bidder Details---------------------------------->

@app.route("/bidderLogin.html")
def blogin():
    return render_template("bidderLogin.html")

@app.route("/adminHome.html")
def ahome():
    return render_template("adminHome.html")

@app.route("/adminLogin.html")
def alogin():
    return render_template("adminLogin.html")

@app.route("/bidderRegistration.html")
def breg():
    return render_template("bidderRegistration.html")

@app.route("/bidderHome.html")
def bhome():
    return render_template("bidderHome.html")

@app.route("/bidder_reg", methods = ['GET','POST'])
def bidder_reg():
   if request.method == 'POST':
    status = bidderRegistration(request.form['fname'],request.form['mobile'],request.form['email'],request.form['password'])
    if status == 1:
        return render_template("bidderLogin.html",m1="sucess")
    else:
        return render_template("bidderRegistration.html",m1="failed")


@app.route("/viewProducts.html")
def view_all_product():
    data = bidder_view_products()
    return render_template("viewProducts.html",products = data)


@app.route("/viewSellers.html")
def view_Sellers():
    data = view_Sellers()
    return render_template("viewProducts.html",products = data)


@app.route("/viewCartProducts.html")
def viewCartProduct():
    data = bidderViewCartProducts()
    print("------------------------DATA--------------------------")
    print(data)
    return render_template("viewCartProducts.html",products = data)


@app.route("/bidder_add_cart/<string:id>", methods = ['GET','POST'])
def bidder_add_cart(id):
    if request.method == 'GET':
        session['p_id']=id
        resul = bidder_add_c(id)
        data = bidderViewCartProducts()
        return render_template("viewCartProducts.html",products = data)

@app.route("/bidder_remove_cart/<string:id>", methods = ['GET','POST'])
def bidder_remove_cart(id):
    if request.method == 'GET':
        session['p_id']=id
        resul = bidder_delete_cart_product_action(id)
        data = bidderViewCartProducts()
        print(resul)
        return render_template("viewCartProducts.html",products = data)

@app.route("/bidding_product/<string:id>", methods = ['GET','POST'])
def bidding_product(id):
    if request.method == 'GET':
        session['p_id']=id
        result = biddingProduct(id)
        bidding_bdr=biddingRequest(id);
       # biddig_dtl=biddingDetails(id)
        print(result)
        return render_template("biddingProducts.html",products = result,rsl_bidding_bdr=bidding_bdr)



#<!-------------------------------------------------Seller Details---------------------------------->

@app.route("/sellerLogin.html")
def slogin():
    return render_template("sellerLogin.html")


@app.route("/sellerRegistration.html")
def sreg():
 	return render_template("sellerRegistration.html")

@app.route("/sellerHome.html")
def shome():
 	return render_template("sellerHome.html")

@app.route("/uploadProduct.html")
def upload_product():
 	return render_template("uploadProduct.html")

@app.route("/viewUploadProduct.html")
def view_u_product():
	data = seller_view_products()
	return render_template("viewUploadProduct.html",products = data)

@app.route("/seller_delete_product/<string:id>", methods = ['GET','POST'])
def seller_delete_product(id):
	if request.method == 'GET':
		session['p_id']=id
		resul = seller_delete_product_action(id)
		data = seller_view_products()
		print(resul)
		return render_template("viewUploadProduct.html",products = data)

@app.route("/viewProductResponse.html")
def viewProductResponse():
 	return render_template("viewProductResponse.html")


@app.route("/viewSellProducts.html")
def viewSellProduct():
 	return render_template("viewSellProducts.html")


@app.route("/upload_product", methods = ['GET','POST'])
def uploadProduct():
   if request.method == 'POST':
      status = upload_product_action(request.form['category'],request.form['p_name'],request.form['specification'],request.form['base_price'],request.form['bid_sdate_time'],request.form['bid_ldate_time'],request.form['file_name'])
   if status == 1:
       return render_template("uploadProduct.html",m1="sucess")
   else:
       return render_template("uploadProduct.html",m2="failed")



@app.route("/seller_reg", methods = ['GET','POST'])
def seller_reg():
   if request.method == 'POST':
   	status = sellerRegistration(request.form['fname'],request.form['mobile'],request.form['email'],request.form['password'])
   	if status == 1:
   		return render_template("sellerLogin.html",m1="sucess")
   	else:
   		return render_template("sellerRegistration.html",m1="failed")


@app.route("/login_act", methods=['GET', 'POST'])
def login_act():
    if request.method == 'POST':
        status = login_action(request.form['email'], request.form['password'])
        print(status)
        if status == 1:
            session['email'] = request.form['email']
            return render_template("sellerHome.html", m1="sucess")
        else:
            return render_template("sellerLogin.html", m1="failed")

@app.route("/blogin_act", methods=['GET', 'POST'])
def blogin_act():
    if request.method == 'POST':
        status = blogin_action(request.form['email'], request.form['password'])
        print("=========================================")
        print(status)
        if status == 1:
            session['email'] = request.form['email']
            return render_template("bidderHome.html", m1="sucess")
        else:
            return render_template("bidderLogin.html", m1="failed")


@app.route("/alogin_act", methods=['GET', 'POST'])
def alogin_act():
    if request.method == 'POST':
        status = alogin_action(request.form['email'], request.form['password'])
        print("=========================================")
        print(status)
        if status == 1:
            session['email'] = request.form['email']
            return render_template("adminHome.html", m1="sucess")
        else:
            return render_template("adminLogin.html", m1="failed")



if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5000)

