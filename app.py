from flask import Flask, jsonify
from extensions import db, jwt  # Import shared objects
from auth import auth_bp  # Import after db initialization

app = Flask(__name__)

# Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///grocery.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "supersecretkey"  # Change for production

# Initialize extensions before importing models
db.init_app(app)
jwt.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Grocery Store API"})

if __name__ == "__main__":
    app.run(debug=True)
