# 🤖 Langchain-Groq Examples 🚀

This repository showcases various examples of using Langchain with the Groq language model. It demonstrates different functionalities, from simple chatbot interactions to complex Retrieval-Augmented Generation (RAG) systems and intelligent agents. This project aims to provide developers with practical examples and clear instructions on how to leverage the power of Langchain and Groq for building innovative applications.

## ✨ Key Features

- **Chatbot Implementation:** A basic chatbot that interacts with the Groq model, maintaining conversation history.
- **Simple Chains:** Demonstrates creating Langchain chains with prompt templates, language models, and output parsers.
- **Tool Calling:** Shows how to define, bind, and call custom tools with an LLM, enabling the model to perform specific tasks.
- **RAG System:** Implements a RAG system to answer questions based on YouTube video transcripts, using vector databases for efficient retrieval.
- **Intelligent Agents:** Creates a simple agent that utilizes web search and weather data retrieval tools, showcasing the ReAct framework.
- **Easy Setup:** Simple instructions to get the project up and running quickly.
- **Clear Examples:** Well-documented code examples that are easy to understand and adapt.

## 🛠️ Tech Stack

| Category    | Technology                      | Description                                                                 |
|-------------|---------------------------------|-----------------------------------------------------------------------------|
| **Language** | Python                          | Primary programming language.                                               |
| **Framework**| Langchain                       | Framework for building applications powered by language models.               |
| **LLM**      | Groq                            | Language model provider.                                                    |
| **Embeddings**| Hugging Face Transformers       | Used for creating text embeddings.                                          |
| **Vector DB** | FAISS                           | Vector database for storing and retrieving embeddings.                      |
| **Web Scraping**| DuckDuckGo Search API, DDGS     | Tools for performing web searches.                                         |
| **API**       | Weatherstack API                | API for fetching weather data.                                              |
| **Utilities** | python-dotenv, pydantic, tiktoken | Utilities for environment variables, data validation, and tokenization.     |
| **Other**     | NumPy, Scikit-learn, pypdf, Supabase, requests | Libraries for numerical computation, machine learning, PDF handling, database interaction, and HTTP requests. |

## 📦 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.7+
- Pip package manager
- An API key for Groq (and potentially other services like Weatherstack, depending on which examples you want to run)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/langchain-groq-examples.git
    cd langchain-groq-examples
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add your API keys and other configuration variables to the `.env` file.  For example:

        ```
        GROQ_API_KEY="YOUR_GROQ_API_KEY"
        WEATHERSTACK_API_KEY="YOUR_WEATHERSTACK_API_KEY"
        GOOGLE_API_KEY = "GOOGLE_API_KEY"
        ```

### Running Locally

Each example is a separate Python file. To run an example, simply execute it using Python:

```bash
python main.py
```

or

```bash
python 2_prompts/4_chatbot.py
```

Adjust the command to run the specific file you are interested in.

## 📂 Project Structure

```
langchain-groq-examples/
├── .env                  # Environment variables (API keys, etc.)
├── 2_prompts/            # Examples related to prompts
│   └── 4_chatbot.py      # Chatbot implementation
├── 5_chains/             # Examples related to Langchain chains
│   └── 1_simple_chain.py # Simple chain example
├── 11_RAG/               # Examples related to Retrieval-Augmented Generation (RAG)
│   └── youtube_bot.py    # RAG system for YouTube transcripts
├── 13_tool caling/       # Examples related to tool calling
│   └── tool_calling.py   # Tool calling example
├── 14_gen ai/            # Examples related to general AI agents
│   └── simple_agent.py   # Simple agent example
├── main.py               # Main entry point (career path guidance)
├── README.md             # This file
└── requirements.txt      # Project dependencies
```


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

If you have any questions or suggestions, feel free to contact me at [abdulraffay2494@gmail.com](mailto:abdulraffay2494@gmail.com).

## 💖 Thanks

Thank you for checking out this project! I hope it helps you learn more about Langchain and Groq.
