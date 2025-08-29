from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    return """
        <h1>Hello, World!</h1>
        <br>
        <p>Nice to see you</p>
        <p>please check</p>
        <a href='/random_fact'>View a random fact!</a><br>
        <a href='/modern_fact'>View a modern fact!</a><br>
        <a href='/coin'>Flip a coin!</a>
    """

# 2nd page
@app.route("/random_fact")
def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    with open(f"fact_list/{txt_name}", "r") as f:
        document = f.read()
    return f"{document}"

# 3rd page (modern_fact)
@app.route("/modern_fact")
def index():
    return render_template("dasar.html")  # file di folder templates

# 4th page (coin flip)
@app.route("/coin")
def coin():
    hasil = random.choice(["Heads", "Tails"])
    return f"Hasil lempar koin: {hasil}"

if __name__ == "__main__":
    app.run(debug=True)
