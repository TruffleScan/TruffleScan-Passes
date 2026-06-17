import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/scan")
def scan():
    return render_template("scan.html")

@app.route("/shillit")
def shillit():
    return render_template("shillit.html")

@app.route("/token")
def token():
    return render_template("token.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/investigate")
def investigate():
    return render_template("investigate.html")

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/nft")
def nft():
    return render_template("nft.html")

@app.route("/wallets")
def wallets():
    return render_template("wallets.html")

@app.route("/saved")
def saved():
    return render_template("saved.html")

@app.route("/monitor")
def monitor():
    return render_template("monitor.html")

@app.route("/academy")
def academy():
    return render_template("academy.html")

@app.route("/theme")
def theme():
    return render_template("theme.html")

@app.route("/tokentheme")
def tokentheme():
    return render_template("tokentheme.html")

@app.route("/branding")
def branding():
    return render_template("branding.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/balance")
def balance():
    return render_template("balance.html")

@app.route("/pro")
def pro():
    return render_template("pro.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/verify")
def verify():
    return render_template("verify.html")

@app.route("/verifynft")
def verifynft():
    return render_template("verifynft.html")

@app.route("/howto")
def howto():
    return render_template("howto.html")

@app.route("/limitations")
def limitations():
    return render_template("limitations.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/login")
def login():
    return render_template("dashboard.html")  # Placeholder until auth is built

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=True)
