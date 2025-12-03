<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Anki for AI</title>
    <script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.8/dist/htmx.min.js"></script>

    <style>
        .progress-container {
            border: 1px solid #ccc;
            width: 300px;
            height: 20px;
            margin-top: 6px;
        }
        .progress-bar {
            background: #4caf50;
            height: 100%;
            width: 0%;
            transition: width 0.3s;
        }
    </style>
</head>

<body>
<h2>Anki for AI - Add Word</h2>

<form hx-post="/add" hx-target="#progress-list" hx-swap="afterbegin">
    <input name="word" placeholder="Input word…" required>
    <button type="submit">Add</button>
</form>

<hr/>

<div id="progress-list"></div>

</body>
</html>
