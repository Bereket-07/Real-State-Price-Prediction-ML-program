from flask import Flask , request , jsonify , Response
import utils

PORT=3000
app = Flask(__name__)
@app.route("/locations",methods=['GET'])
def display():
    return utils.get_location()

@app.route("/prediction",methods=["POST"])
def predict_price():
    print(request.json.get('location'))
    location = request.json.get('location')
    sqft = float(request.json.get('sqft'))
    print(sqft)
    bhk = float(request.json.get('bhk'))
    bath = float(request.json.get('bhk'))
    response = jsonify({
        'prediction':utils.get_estimated_price(location,sqft,bhk,bath)
    })
    return response
if __name__=="__main__":
    print(f"the server is running on port{PORT}")
    app.run()