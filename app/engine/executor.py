import uuid
from typing import Dict, Any
from .graph import Graph

RUNS = {}  # in-memory run store


class GraphExecutor:

    async def execute(self, graph: Graph, state: Dict[str, Any]):
        run_id = str(uuid.uuid4())
        execution_log = []
        RUNS[run_id] = {"state": state, "log": execution_log}

        current = graph.start_node

        while current:
            node = graph.nodes[current]
            execution_log.append(f"Running {current}")

            state = await node.run(state)
            RUNS[run_id]["state"] = state

            # Branching and Looping
            next_node = graph.edges.get(current)

            if isinstance(next_node, dict):  # conditional routing
                for condition, nxt in next_node.items():
                    if eval(condition, {}, state):  
                        current = nxt
                        break
                else:
                    current = None
            else:
                current = next_node

        return run_id, state, execution_log
