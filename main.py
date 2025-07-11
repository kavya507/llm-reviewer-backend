from fastapi import FastAPI
from app.models import ReviewRequest
from app.chains import get_summary_chain
from app.utils import extract_pros_cons
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chain = get_summary_chain()

@app.get("/")
def home():
    return {"message":"Welcome to docs, to test the API"}

@app.post("/summarize")
async def summarize_reviews(request: ReviewRequest):
    joined = "\n".join(request.reviews)
    result = chain.run(reviews=joined)
    pros, cons = extract_pros_cons(result)
    return {"pros": pros, "cons": cons}