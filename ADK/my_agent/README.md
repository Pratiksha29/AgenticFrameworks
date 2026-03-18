

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ 
- Google ADK installed
- Google Cloud project with Vertex AI API enabled
- Valid Google Cloud credentials

### Setup

1. **Navigate to the ADK directory**:
   ```bash
   cd /<your-project-dir/>AgenticFrameworks/ADK
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the agent directory**:
   ```bash
   cd my_agent
   ```

5. **Set up Google Cloud credentials** (if not already done):
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
   # OR use Application Default Credentials
   gcloud auth application-default login
   ```

6. **Run the agent**:
   ```bash
   cd ..
   adk run my_agent
   ```

7. **Or use the web interface**:
   ```bash
   adk web --port 8000
   # Then open http://localhost:8000 in your browser    
   ```

## 💬 Usage Examples

Once the agent is running, you can ask:

```
[user]: what all can you do?
[agent]: I can tell you the current weather conditions for a specified city, and I can also provide the current time in a specified city.

[user]: tell me weather in New York
[agent]: The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit).

[user]: what time is it in New York?
[agent]: The current time in New York is 2026-03-18 11:30:00 EDT-0400
```

## 🛠 Available Tools

### 1. Weather Tool (`get_weather`)
- **Purpose**: Get current weather information
- **Supported Cities**: Currently supports New York (can be extended)
- **Returns**: Weather report with temperature and conditions

### 2. Time Tool (`get_current_time`)
- **Purpose**: Get current time in different timezones
- **Supported Cities**: Currently supports New York (can be extended)
- **Returns**: Current date, time, and timezone information





## 📚 Learn More

- [Google ADK Documentation](https://cloud.google.com/agent-development-kit)
- [Vertex AI Models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
- [Google Cloud Authentication](https://cloud.google.com/docs/authentication)
