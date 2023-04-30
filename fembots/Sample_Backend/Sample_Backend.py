from flask import Flask, request

app = Flask(__name__)


@app.post("/book")
def book():
    try:
        data = dict(request.get_json())
        return {"message": f"Booked {data['mode']} {data['start']} {data['end']}"}, 201
    except:
        return {"message": "Not Booked"}, 415


@app.post("/pay")
def pay():
    try:
        data = dict(request.get_json())
        return {"message": f"Payment mode confirmed {data['mode']}"}, 201
    except:
        return {"message": "Payment mode not confirmed"}, 415


app.run()
