import requests

response = requests.post("http://localhost:5000", data={"question": "Show all students"})
print("Response Text:")
print(response.text[:2000])  # Print first 2000 characters
print(f"\nResponse Length: {len(response.text)}")
