from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_URL = "https://www.thecocktaildb.com/api/json/v1/1/"


@app.route("/", methods=["GET", "POST"])
def index():
    drinks = None
    query = ""
    if request.method == "POST":
        query = request.form["cocktail"]
        params = {"s": query}
        response = requests.get(API_URL + "search.php", params=params)
        if response.status_code == 200:
            data = response.json()
            drinks = data.get("drinks")
            print(drinks)
    return render_template("search_result.html", drinks=drinks, query=query)


if __name__ == "__main__":
    app.run(debug=True)



