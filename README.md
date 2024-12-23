# LangChain SQL Database Chat Application 🦜

A Streamlit-based interactive application that allows users to query SQL databases using natural language. Powered by LangChain and Groq's LLM, this application supports both SQLite and MySQL databases.

## Features 🌟

- Natural language queries to SQL databases
- Support for both SQLite and MySQL databases
- Interactive chat interface
- Real-time streaming responses
- Persistent chat history

## Prerequisites 📋

- Groq API key
- For MySQL: Valid MySQL database credentials
- For SQLite: Access to the local database file (`sales_data_warehouse.db`)

## Installation 🔧

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required packages:
```bash
pip install streamlit langchain langchain-groq sqlalchemy mysql-connector-python
```

## Environment Setup 🛠️

1. Ensure you have a valid Groq API key
2. If using MySQL, prepare your database connection details:
   - Host
   - Username
   - Password
   - Database name
3. If using SQLite, ensure your database file is in the correct location

## Usage 💻

1. Start the application:
```bash
streamlit run app.py
```

2. In the sidebar:
   - Choose your database type (SQLite or MySQL)
   - If using MySQL, enter your database credentials
   - Enter your Groq API key

3. Start chatting with your database using natural language!

## Features Breakdown 🔍

### Database Configuration
- Supports both SQLite and MySQL databases
- Secure credential handling

### Chat Interface
- Persistent chat history
- Stream-based response generation
- Clear message history option
- User-friendly chat input


## Code Structure 📚

- Database Configuration:
  - Supports two database types (SQLite/MySQL)
  - Uses SQLAlchemy for database connections

- LangChain Integration:
  - Uses Groq's LLM (Llama3-8b-8192 model)
  - Implements SQL Database Toolkit
  - Zero-shot agent for query processing

- Streamlit UI:
  - Sidebar for configuration
  - Chat interface for interactions
  - Streaming response display

## Limitations and Considerations ⚠️

- Requires a valid Groq API key


