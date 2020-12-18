from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_location_names',methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

@app.route('/predict_home_price',methods = ['GET', 'POST'])
def predict_home_price():
    # for HTTP form we use request
    if request.method == 'POST':
        sqft = float(request.form['sqft'])
        # location = request.form['location']
        location = request.form.get('location')
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        prediction = util.get_estimated_price(location, sqft, bhk, bath)

        return render_template('home.html',prediction_text = "The Predicted house Price is Rs.{} lakhs".format(prediction))
    return render_template("home.html")

    # response = jsonify({
    #     'estimated price': util.get_estimated_price(location, total_sqft, bhk, bath)
    # })
    #
    # return response

if __name__=='__main__':
    print("Starting Python Flask Server for House Price Prediction of Bangalore City")
    util.load_saved_artifacts()
    app.run(debug=True)