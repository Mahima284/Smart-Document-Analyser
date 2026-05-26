from flask import Flask, render_template, request
import os

from utils.extractor import extract_text
from utils.summarizer import summarize_text
from utils.ner import extract_entities
from utils.classifier import classify_document
from utils.anomaly import detect_anomalies

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route('/')
def home():

    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['document']

    if file:

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        text = extract_text(filepath)

        word_limit = int(request.form['word_limit'])

        summary = summarize_text(text, word_limit)

        entities = extract_entities(text)

        doc_type = classify_document(text)

        anomalies = detect_anomalies(text)

        return render_template(
            "index.html",
            summary=summary,
            entities=entities,
            doc_type=doc_type,
            anomalies=anomalies
        )

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)