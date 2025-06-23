# Cerebras Chat Completion Example

This project demonstrates how to use the Cerebras SDK to generate chat completions using the Llama 4 model.

## Prerequisites

- Python 3.8+
- Cerebras API key (get it from [Cerebras Console](https://console.cerebras.net/))

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Cerebras API key as an environment variable:
   ```bash
   # On macOS/Linux
   export CEREBRAS_API_KEY='your-api-key-here'
   
   # On Windows (Command Prompt)
   set CEREBRAS_API_KEY=your-api-key-here
   
   # On Windows (PowerShell)
   $env:CEREBRAS_API_KEY='your-api-key-here'
   ```

## Usage

Run the chat completion example:

```bash
python cebras.py
```

## Environment Variables

- `CEREBRAS_API_KEY`: Your Cerebras API key (required)

## Example

The script will send a chat completion request to the Cerebras API and stream the response to the console.
