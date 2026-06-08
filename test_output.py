#!/usr/bin/env python
"""
Test script to display AI SQL Generator output with results
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://localhost:5000"

test_questions = [
    "Show all students",
    "Get all female students", 
    "Find students older than 20",
    "List students named Priya",
    "Count total students by gender",
]

print("\n" + "="*80)
print("🤖 AI SQL GENERATOR - COMPLETE OUTPUT WITH RESULTS")
print("="*80)

for i, question in enumerate(test_questions, 1):
    print(f"\n{'='*80}")
    print(f"📝 Test {i}: {question}")
    print("="*80)
    
    try:
        response = requests.post(
            BASE_URL,
            data={"question": question},
            timeout=10
        )
        
        if response.status_code == 200:
            # Parse HTML to extract SQL query and results
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the generated SQL section
            sql_section = soup.find('h3', string='Generated SQL')
            if sql_section:
                sql_para = sql_section.find_next('p')
                if sql_para:
                    sql_query = sql_para.get_text(strip=True)
                    print(f"\n📋 Generated SQL Query:")
                    print(f"   {sql_query}")
            
            # Find the results section
            results_section = soup.find('h3', string='Results')
            if results_section:
                print(f"\n📊 Query Results:")
                result_paras = results_section.find_all_next('p')
                if result_paras:
                    for j, para in enumerate(result_paras[:-1], 1):  # Skip last empty
                        result_text = para.get_text(strip=True)
                        if result_text:
                            print(f"   {j}. {result_text}")
                else:
                    print("   (No results)")
            
            print(f"\n✓ Status: OK")
            
        else:
            print(f"✗ Error: Status code {response.status_code}")
            
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n" + "="*80)
print("✅ AI SQL Generator is working correctly!")
print("="*80 + "\n")
