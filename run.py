from app import create_app
from flask import request, jsonify

app = create_app()

@app.route("/prueba", methods=["GET"])
def prueba():
    j=jsonify(id="1",email="n@n.com")
    return j, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
