import enum
from time import sleep

from langgraph.graph import StateGraph, MessagesState, START, END


class GraphStatus(enum.Enum):
    IDLE = "idle"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"


class State(MessagesState):
    status: GraphStatus
    iterations: int


def slow_node(state: State) -> State:
    sleep(3)
    state["status"] = GraphStatus.RUNNING
    return state


def agent(state: State) -> State:
    return state


def metrics(state: State) -> State:
    state["status"] = GraphStatus.FINISHED
    return state


# Instantiate new workflow
workflow = StateGraph(State)

# Add workflow nodes
workflow.add_node("slow", slow_node)
workflow.add_node("agent", agent)
workflow.add_node("metrics", metrics)

# Add workflow edges
workflow.add_edge(START, "slow")
workflow.add_edge("slow", "agent")
workflow.add_edge("agent", "metrics")
workflow.add_edge("metrics", END)

# Compile the final graph
graph = workflow.compile()

__all__ = ["graph", "State", "GraphStatus"]
