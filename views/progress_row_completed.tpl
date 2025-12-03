<div id="task-{{task_id}}" hx-get="/progress/{{task_id}}" hx-trigger="stop" hx-swap="outerHTML">
    <p><b>{{word}}</b> — {{status}}</p>

    <div class="progress-container">
        <div class="progress-bar" style="width: {{percent}}%;"></div>
    </div>
</div>
