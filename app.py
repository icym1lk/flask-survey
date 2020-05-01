from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "passphrase"
debug = DebugToolbarExtension(app)

from surveys import satisfaction_survey 
responses = []

@app.route("/")
def root():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    return render_template("index.html", survey_title=survey_title, survey_instructions=survey_instructions)
    
