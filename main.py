from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from JSON
with open(os.path.join(os.path.dirname(__file__), "q-vercel-python.json"), "r") as f:
    student_data = json.load(f)

@app.get("/api")
def get_marks(request: Request):
    """
    Usage: GET /api?name=Alice&name=Bob
    Returns JSON: { "marks": [10, 20] }
    """
    names = request.query_params.getlist("name")  # getlist returns multiple "name" params
    marks_list = []

    for name in names:
        # If student not found, we can return None or skip
        mark = student_data.get(name, None)
        marks_list.append(mark)

    return {"marks": marks_list}
