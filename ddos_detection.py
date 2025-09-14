import requests
import json
import time 


def send_alert(analysis_result):
    webhook_url = "https://hook.us1.make.com/3ard4i462w19jgt2bt8etkyirzb14ar7"
    payload = {
        "checkout_url": analysis_result
    }
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Alert sent successfully.")
        else:
            print(f"Failed to send alert: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending alert: {e}")


def analyze_logs_with_ollama(log_data):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": f"""
You are a ddos log analysis assistant. I have a log file from a Flask web server, and I need you to analyze it for potential DDoS attacks. The criteria for detection are as follows:

- Identify any IP address that has made more than 10 requests within 10 seconds.
- If such an IP address is found, respond with the IP address and the number of requests made during that second.
- If no DDoS attacks are detected, simply reply with "No DDoS detected." OR if ddos is found reply with "DDoS is found , ip address and number of request within timestamp".
- Just reply with ddos is found or not , dont give extra info 

Here are the logs for analysis:
{log_data}
"""

            }
        ],
        "stream": False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        analysis_result = response.json()
        print("Analysis Result:", analysis_result['message']['content'])
        if "found" in analysis_result['message']['content']:
            send_alert(analysis_result=f"Analysis Result : {analysis_result['message']['content']}")
    else:
        print("Error:", response.status_code, response.text)



log_data = []

try:
    with open("webserver_logs.log", "r") as f:
        log_data = f.read()
except FileNotFoundError as e:
    print(f"File not Found: {e}")

if log_data:
    analyze_logs_with_ollama(log_data)
else:
    print("No log is found")
