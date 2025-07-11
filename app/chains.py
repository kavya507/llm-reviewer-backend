from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from app.config import OPENAI_API_KEY

def get_summary_chain():
    prompt = ChatPromptTemplate.from_template("""
    
    You are a helpful and concise AI assistant. Analyze the customer reviews below and summarize the top 5 most frequently mentioned pros and cons about the product’s quality, design, features, and performance.

    ❌ Do NOT include anything about shipping, packaging, customer service, or review formatting.

    ✅ Format the output exactly like this:

    Pros:
    - ...

    Cons:
    - ...

    ⚠️ Do NOT forget to include both headers: "Pros:" and "Cons:"
    ⚠️ Each point must be on its own line, starting with a dash (-)

    {reviews}


    """)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6, openai_api_key=OPENAI_API_KEY)
    return LLMChain(llm=llm, prompt=prompt)
