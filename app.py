from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("JobScrapper")

# fake db
db = {}


@app.route('/')
def hello_world():
    return render_template("Home.html")


@app.route('/report')
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existing_Jobs = db.get(word)
        if existing_Jobs:
            jobs = existing_Jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception();
        word = word.lower()
        jobs = db.get(word)
        if not word:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
        return f"Generate CSV for {word}"

    except:
        return redirect("/")


if __name__ == '__main__':
    app.run()
