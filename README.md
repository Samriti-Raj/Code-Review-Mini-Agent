# Minimal Workflow Engine (AI Engineering Assignment)

This project implements a simplified workflow/graph engine similar to LangGraph.

## Features
- Nodes (async Python functions)
- Shared state dictionary
- Edges defining execution order
- Branching via conditional expressions
- Looping support
- Tool registry
- FastAPI endpoints

## Endpoints
POST /graph/create  
POST /graph/run  
GET /graph/state/{run_id}

## Example Workflow (Code Review Mini-Agent)
1. Extract functions  
2. Check complexity  
3. Detect issues  
4. Suggest improvements  
5. Loop until quality_score >= threshold

## How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## What I Would Improve
- Replace eval-based conditions with a safe expression evaluator  
- Add WebSockets for live streaming logs  
- Add SQLite persistence for runs  
- Add concurrency for parallel nodes  
