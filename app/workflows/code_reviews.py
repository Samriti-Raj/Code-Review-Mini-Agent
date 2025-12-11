from app.engine.node import Node
from app.engine.registry import tool_registry
from typing import Dict, Any


# --- Tools ---
def count_functions(code: str):
    return code.count("def ")


def calc_complexity(code: str):
    return code.count("if") + code.count("for") + code.count("while")


def detect_issues(code: str):
    issues = 0
    if "TODO" in code:
        issues += 1
    return issues


def suggest_improvements(complexity: int, issues: int):
    score = max(0, 10 - complexity - issues)
    return score


tool_registry.register("count_functions", count_functions)
tool_registry.register("complexity", calc_complexity)
tool_registry.register("issues", detect_issues)
tool_registry.register("suggest", suggest_improvements)


# --- Nodes ---
async def extract_functions(state: Dict[str, Any]):
    code = state["code"]
    state["function_count"] = tool_registry.get("count_functions")(code)
    return state


async def check_complexity(state: Dict[str, Any]):
    code = state["code"]
    state["complexity"] = tool_registry.get("complexity")(code)
    return state


async def detect_basic_issues(state: Dict[str, Any]):
    code = state["code"]
    state["issues"] = tool_registry.get("issues")(code)
    return state


async def suggest_improvement(state: Dict[str, Any]):
    score = tool_registry.get("suggest")(state["complexity"], state["issues"])
    state["quality_score"] = score
    return state


def build_workflow():
    nodes = {
        "extract": Node("extract", extract_functions),
        "complexity": Node("complexity", check_complexity),
        "issues": Node("issues", detect_basic_issues),
        "suggest": Node("suggest", suggest_improvement),
    }

    edges = {
        "extract": "complexity",
        "complexity": "issues",
        "issues": "suggest",
        "suggest": {
            "quality_score < 7": "issues"
  # loop until quality improves
        }
    }

    return nodes, edges, "extract"
