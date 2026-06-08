#!/usr/bin/env python
import sys
import traceback

print("Starting test...", file=sys.stderr)

try:
    print("Step 1: Importing Flask", file=sys.stderr)
    from flask import Flask, render_template, request
    print("✓ Flask imported", file=sys.stderr)
    
    print("Step 2: Importing sqlite3", file=sys.stderr)
    import sqlite3
    print("✓ sqlite3 imported", file=sys.stderr)
    
    print("Step 3: Importing google.generativeai", file=sys.stderr)
    import google.generativeai as genai
    print("✓ google.generativeai imported", file=sys.stderr)
    
    print("Step 4: Creating Flask app", file=sys.stderr)
    app = Flask(__name__)
    print("✓ Flask app created", file=sys.stderr)
    
    print("Step 5: Configuring API", file=sys.stderr)
    genai.configure(api_key="YOUR_API_KEY_HERE")
    print("✓ API configured", file=sys.stderr)
    
    print("Step 6: Creating model", file=sys.stderr)
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("✓ Model created", file=sys.stderr)
    
    print("\nAll checks passed! App is ready to run.", file=sys.stderr)
    print("To start the app, run: python app.py", file=sys.stderr)
    print("Then access http://localhost:5000", file=sys.stderr)
    
except Exception as e:
    print(f"✗ Error: {e}", file=sys.stderr)
    traceback.print_exc()
    sys.exit(1)
