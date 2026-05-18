from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory message store (resets on restart)
messages = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if name and email and message:
            messages.append({"name": name, "email": email, "message": message})
            return redirect(url_for("contact", success=1))
    return render_template("contact.html", messages=messages, success=request.args.get("success"))

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
