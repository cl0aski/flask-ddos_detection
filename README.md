Installation & Setup
Prerequisites
Python 3.x

Ollama installed and running locally

Llama3 model downloaded in Ollama

Installation Steps
Clone the repository:

bash
git clone <your-repo-url>
cd ddos-detection
Install required dependencies:

bash
pip install requests
Set up Ollama:

bash
# Install Ollama (if not already installed)
# Visit https://ollama.ai for installation instructions

# Pull the Llama3 model
ollama pull llama3
Configure the webhook URL:

Replace the webhook_url in the script with your Make.com webhook URL

Usage
Ensure your web server logs are being written to webserver_logs.log

Run the script:

bash
python ddos_detection.py
Configuration
Adjust the threshold values in the prompt (currently set to 10 requests within 10 seconds)

Modify the webhook URL to point to your alerting system

File Structure
text
ddos-detection/
├── ddos_detection.py  # Main detection script
├── webserver_logs.log # Web server log file (not included in repo)
├── README.md          # This file
└── requirements.txt   # Python dependencies
Requirements
Create a requirements.txt file with:

text
requests>=2.25.0
Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request

License
MIT License - feel free to use this code for your projects.

Notes
Ensure your Ollama server is running on http://localhost:11434

The script expects Flask web server logs in the specified format

Regularly update the Llama3 model for improved detection capabilities
