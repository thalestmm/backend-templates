from typing import Optional
from time import sleep

from celery import Celery
from celery.utils.log import get_task_logger

from app.core.config import settings
from app.graphs.main import State, GraphStatus, graph

logger = get_task_logger(__name__)

app = Celery(
    "tasks",
    backend=settings.BACKEND_URL,
    broker=settings.BROKER_URL,
)


@app.task(name="tasks.invoke_graph")
def invoke_graph(state: Optional[State] = None) -> None:
    """
    Sample langgraph graph invocation
    :param state: Initial state to instantiate the graph
    :return:
    """
    logger.info("Invoking langgraph graph...")
    if state is None:
        state = State(status=GraphStatus.IDLE)

    _ = graph.invoke(state=state)

    return None
