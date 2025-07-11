# LLM Reviewer

A FastAPI application for summarizing customer reviews using advanced language models and agents. This project supports multilingual reviews by automatically detecting and translating non-English reviews to English before analysis.

## Features
- **Multilingual Support:** Detects and translates reviews in any language to English.
- **Review Summarization:** Extracts the top pros and cons from customer reviews using LLMs.
- **API-First:** Exposes endpoints for easy integration with other services or frontends.
- **Agent Architecture:** Modular agents for language detection, translation, and review analysis.

## Tech Stack
- **FastAPI** for the web API
- **LangChain** for LLM orchestration and agent management
- **OpenAI API** for language model access
- **python-dotenv** for environment variable management
- **Pydantic** for data validation

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd LLM_Reviewer
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root with your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API docs:**
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## API Usage

### `POST /summarize`
Summarizes a list of customer reviews.

**Request Body:**
```json
{
  "reviews": [
    "Great product!", 
    "Muy bueno, me encantó.",
    "Nicht so gut, leider enttäuscht."
  ]
}
```

**Response:**
```json
{
  "pros": ["..."],
  "cons": ["..."]
}
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE) 