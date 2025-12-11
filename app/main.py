from fastapi import FastAPI
from app.engine.executor import GraphExecutor, RUNS
from app.engine.graph import Graph
from app.models import CreateGraphRequest, RunGraphRequest
from app.workflows.code_reviews import build_workflow

app = FastAPI()

GRAPHS = {}
executor = GraphExecutor()


@app.post("/graph/create")
async def create_graph(req: CreateGraphRequest):
    if req.workflow == "code_review":
        nodes, edges, start = build_workflow()

    graph_id = f"graph_{len(GRAPHS)}"
    GRAPHS[graph_id] = Graph(nodes, edges, start)
    return {"graph_id": graph_id}


@app.post("/graph/run")
async def run_graph(req: RunGraphRequest):
    graph = GRAPHS[req.graph_id]
    run_id, final_state, log = await executor.execute(graph, req.initial_state)
    return {"run_id": run_id, "final_state": final_state, "log": log}


@app.get("/graph/state/{run_id}")
async def get_state(run_id: str):
    return RUNS.get(run_id, {})
