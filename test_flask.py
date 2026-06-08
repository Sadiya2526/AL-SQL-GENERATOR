from flask import Flask, render_template, request
import sqlite3
import sys
import os

# Get the absolute path to the templates directory
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/test")
def test():
    try:
        html = render_template("test.html", sql_query="SELECT * FROM students")
        print(f"Test template rendered, length: {len(html)}", file=sys.stderr)
        return html
    except Exception as e:
        import traceback
        traceback.print_exc(file=sys.stderr)
        return f"Error: {e}"

@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
