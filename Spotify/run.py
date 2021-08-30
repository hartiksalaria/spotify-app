from flask import Flask, render_template, request, flash, redirect, url_for
from forms import SongLink
from main import add_song
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config["SECRET_KEY"] = "somegibberish"
csrf = CSRFProtect(app)


@app.route("/", methods=["POST", "GET"])
def home():
    form = SongLink(request.form)
    if request.method == "POST" and form.validate():
        if add_song(items=[form.song_link.data]):
            flash("Added successfully. Thanks for recommending the song ! ", "alert alert-success")
        else:
            flash("Wrong link. Song doesn't exist !", "alert alert-warning")
        return redirect(url_for('home'))
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
