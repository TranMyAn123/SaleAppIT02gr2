from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    print(q)
    prods = dao.load_products(q=q)
    cates = dao.load_categories()
    return render_template("index.html", cates=cates, prods=prods)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)