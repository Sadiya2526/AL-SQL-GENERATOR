import requests

# Test GET request
response = requests.get("http://localhost:5000")
print(f"GET Response Status: {response.status_code}")
print(f"GET Response Length: {len(response.text)}")
print("GET Response Text (first 1000 chars):")
print(response.text[:1000])

print("\n" + "="*80 + "\n")

# Test POST request
response = requests.post("http://localhost:5000", data={"question": "Show all students"})
print(f"POST Response Status: {response.status_code}")
print(f"POST Response Length: {len(response.text)}")
print("POST Response Text (first 1000 chars):")
print(response.text[:1000])
