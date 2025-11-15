from app.worker.tasks import quick_task, invoke_graph


if __name__ == "__main__":
    for i in range(200):
        _ = quick_task.delay()
        _ = quick_task.delay()
        _ = invoke_graph.delay()
