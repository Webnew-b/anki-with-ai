from __future__ import annotations

import threading
import uuid
from typing import Dict, TypedDict, Any

from bottle import Bottle, run, template, request, static_file, response  # type: ignore

import pipeline


class TaskState(TypedDict):
    word: str
    status: str
    percent: int


app = Bottle()

TASKS: Dict[str, TaskState] = {}


@app.route("/static/<path:path>")
def static_files(path: str) -> Any:
    # Bottle's static_file 返回类型不是字符串，而是 Bottle Response 对象
    return static_file(path, root="./static")


@app.get("/")
def index() -> str:
    return template("index")


@app.post("/add")
def add_word() -> str:
    pipe: pipeline.Pipeline = app.config["pipeline"]
    word_raw = request.forms.get("word")

    if word_raw is None:
        return "<p>Error: word is required</p>"

    word = word_raw.strip()
    task_id = str(uuid.uuid4())

    TASKS[task_id] = TaskState(
        word=word,
        status="queued",
        percent=0,
    )

    # 创建后台线程（注意类型标注）
    thread = threading.Thread(
        target=process_task,
        args=(task_id, pipe,),
        daemon=True,
    )
    thread.start()

    return template(
        "progress_row",
        task_id=task_id,
        word=word,
        status="queued",
        percent=0
    )


@app.get("/progress/<task_id>")
def get_progress(task_id: str) -> str:
    task = TASKS.get(task_id)
    if task is None:
        response.status = 404
        return f"<p>Task {task_id} not found.</p>"

    # 如果任务失败，前端渲染 error 区块
    if task.get("status") == "error":
        response.status = 500
        return template(
            "progress_row_error",
            task_id=task_id,
            word=task["word"],
        )

    return template(
        "progress_row",
        task_id=task_id,
        word=task["word"],
        status=task["status"],
        percent=task["percent"]
    )


def process_task(task_id: str, pipe: pipeline.Pipeline) -> None:
    word = TASKS[task_id]['word']

    def reporter(status: str, percent: int) -> None:
        task = TASKS.get(task_id)
        if task is None:
            return
        task["status"] = status
        task["percent"] = percent

    try:
        _ = pipe.run(word, progress=reporter)

        TASKS[task_id]["status"] = "completed"
        TASKS[task_id]["percent"] = 100

    except Exception as exc:
        TASKS[task_id]["status"] = "error"
        TASKS[task_id]["percent"] = 100
        print(exc)

    TASKS[task_id]['status'] = 'completed'
    TASKS[task_id]['percent'] = 100


def start(pipe: pipeline.Pipeline) -> None:
    app.config["pipeline"] = pipe
    run(app, host="0.0.0.0", port=8080, debug=True, reloader=True)
