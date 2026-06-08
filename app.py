from flask import Flask, render_template, request
import sqlite3
import sys
import os

# Get the absolute path to the templates directory
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
print(f"Template directory: {template_dir}", file=sys.stderr)
print(f"Template directory exists: {os.path.exists(template_dir)}", file=sys.stderr)

app = Flask(__name__, template_folder=template_dir)

def generate_sql_query(question):
    """
    Generate SQL query from natural language question
    (Mock implementation for demo purposes)
    """
    question_lower = question.lower()
    
    # Simple rule-based SQL generation for demo
    if "show all" in question_lower or "list all" in question_lower:
        return "SELECT * FROM students"
    elif "female" in question_lower:
        return "SELECT * FROM students WHERE gender = 'Female'"
    elif "male" in question_lower:
        return "SELECT * FROM students WHERE gender = 'Male'"
    elif "older than" in question_lower:
        # Extract age from question
        words = question_lower.split()
        for i, word in enumerate(words):
            if word == "than" and i + 1 < len(words):
                try:
                    age = int(words[i + 1])
                    return f"SELECT * FROM students WHERE age > {age}"
                except:
                    pass
        return "SELECT * FROM students WHERE age > 20"
    elif "priya" in question_lower or "name" in question_lower:
        return "SELECT * FROM students WHERE name = 'Priya'"
    elif "count" in question_lower and "gender" in question_lower:
        return "SELECT gender, COUNT(*) as count FROM students GROUP BY gender"
    elif "youngest" in question_lower:
        return "SELECT * FROM students ORDER BY age ASC LIMIT 1"
    elif "oldest" in question_lower:
        return "SELECT * FROM students ORDER BY age DESC LIMIT 1"
    elif "average age" in question_lower:
        return "SELECT AVG(age) as average_age FROM students"
    else:
        return "SELECT * FROM students"

print("✓ Mock SQL generator initialized (Demo Mode)", file=sys.stderr)

def run_query(query):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return rows

@app.route("/", methods=["GET","POST"])
def home():

    sql_query = ""
    result = []

    if request.method == "POST":
        try:
            question = request.form.get("question", "")
            print(f"Processing question: {question}", file=sys.stderr)

            # Generate SQL query using mock implementation
            sql_query = generate_sql_query(question)
            print(f"Generated SQL: {sql_query}", file=sys.stderr)

            try:
                result = run_query(sql_query)
                print(f"Query results: {result}", file=sys.stderr)
            except Exception as e:
                result = [(f"Error: {str(e)}",)]
                print(f"Query error: {e}", file=sys.stderr)
        except Exception as e:
            print(f"POST handler error: {e}", file=sys.stderr)
            result = [(f"Error: {str(e)}",)]

    try:
        html = render_template(
            "index.html",
            sql_query=sql_query,
            result=result
        )
        print(f"Template rendered successfully, length: {len(html)}", file=sys.stderr)
        return html
    except Exception as e:
        import traceback
        print(f"Template rendering error: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return f"<h1>Error rendering template</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    print("\n" + "="*60, file=sys.stderr)
    print("🚀 AI SQL Generator is starting...", file=sys.stderr)
    print("📧 Open http://localhost:5000 in your browser", file=sys.stderr)
    print("="*60 + "\n", file=sys.stderr)
    app.run(debug=True, host='localhost', port=5000)