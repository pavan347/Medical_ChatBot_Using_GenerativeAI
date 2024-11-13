from flask import Flask

from modules import  routes

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")

# Register blueprints
app.register_blueprint(routes.bp)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
