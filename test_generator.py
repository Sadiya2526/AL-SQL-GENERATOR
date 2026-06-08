#!/usr/bin/env python
"""
Test script to demonstrate AI SQL Generator functionality
Makes requests to the running Flask app and shows output
"""

import requests
import json

# Base URL of the Flask app
BASE_URL = "http://localhost:5000"

# Sample questions to test
test_questions = [
    "Show all students",
    "Get all female students",
    "Find students older than 20",
    "List students named Priya",
    "Count total students by gender",
]

print("\n" + "="*70)
print("🤖 AI SQL GENERATOR - TEST OUTPUT")
print("="*70)

for i, question in enumerate(test_questions, 1):
    print(f"\n📝 Test {i}: {question}")
    print("-" * 70)
    
    try:
        # Send POST request with the question
        response = requests.post(
            BASE_URL,
            data={"question": question},
            timeout=10
        )
        
        # Parse the response
        # Extract SQL query and results from the HTML (simplified)
        if response.status_code == 200:
            # The response contains HTML, but we can see the generated content
            print("✓ Request successful!")
            print(f"  Status Code: {response.status_code}")
            print(f"  Response Length: {len(response.text)} characters")
            
            # You can also see the form submission worked
            if "Generated SQL" in response.text:
                print("  ✓ Generated SQL found in response")
            if "Results" in response.text:
                print("  ✓ Results section found in response")
        else:
            print(f"✗ Request failed with status code: {response.status_code}")
            
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n" + "="*70)
print("📊 To see the full interactive interface:")
print("   1. Open http://localhost:5000 in your web browser")
print("   2. Enter questions about students database")
print("   3. Click 'Generate' to see SQL queries and results")
print("="*70 + "\n")
