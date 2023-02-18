from flask import Flask,send_file,render_template, request
import os

REST_URL = os.environ.get("REST_URL", "http://localhost/feedback")

app = Flask(__name__)

@app.route("/about")
@app.route("/")
def about():
    return render_template("about.html.j2")

@app.route("/workshop")
def project_materials():
    return render_template("workshop.html.j2")

@app.route("/photo")
def photo():
    return render_template("photo.html.j2")    

#@app.route("/feedback")
#def feedback():
#    return render_template("feedback.html.j2")    

@app.route("/download")   
def download_file():
    p = "static/correspondence_kurakin.csv"
    return send_file(p, as_attachment=True)

@app.route("/download_2")   
def download_file_2():
    p = "static/people_kurakin.csv"
    return send_file(p, as_attachment=True)

@app.route("/feedback", methods=["GET", "POST"])   
def people():
    if request.method == 'POST':
        lastname = request.values.get("lastname")
        suggestions = request.values.get("suggestions")
    requests.post(REST_URL, json={"lastname": lastname, "suggestions": suggestions})
    result = requests.get(REST_URL).json()
    return render_template("feedback_2.html.j2", result=result) 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
