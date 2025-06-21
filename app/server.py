from flask import Flask, request, render_template
from Generate_Summary import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    url = request.form.get("url", "")
    if not url:
        return render_template("home.html", summary="No URL provided", full_text="")

    summary, full_text = summarize_text(url)
    return render_template("home.html", summary=summary, full_text=full_text)

if __name__ == "__main__":
    app.run(debug=True)
