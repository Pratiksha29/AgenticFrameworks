

# Google Agent Development Kit (ADK) Project

This project contains agents built using Google's Agent Development Kit (ADK).

## 🔑 API Key & Setup Instructions

### 1. Get Google Cloud Project ID
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project from the project dropdown
3. Copy the **Project ID** (not Project Name)

### 2. Get Google AI API Key
1. Visit [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Select or create a Google Cloud project
5. Copy the generated API key (starts with `AIza`)

### 3. Set Up Environment Variables
Create a `.env` file in the ADK directory:
```bash
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Google AI Configuration
GOOGLE_AI_API_KEY=your-api-key-here

# Optional: Service Account Key
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
```

### 4. Set Up Google Cloud Credentials
**Option A:** Service Account Key
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

**Option B:** Application Default Credentials
```bash
gcloud auth application-default login
```

### 5. Enable Required APIs
Make sure these APIs are enabled in your Google Cloud project:
- Vertex AI API
- Generative Language API

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

- [Google ADK Documentation](https://google.github.io/adk-docs/tutorials/agent-team/)
- [Google AI Studio](https://aistudio.google.com) - Create API keys and test models
- [Vertex AI Models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
- [ADK Agent Team Tutorial](https://google.github.io/adk-docs/tutorials/agent-team/)



