from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Background Example</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #3498db;  /* Flat UI Blue */
                font-family: Arial, sans-serif;
            }
            .container {
                text-align: center;
                padding: 40px;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #2c3e50;  /* Flat UI Midnight Blue */
                margin-bottom: 20px;
            }
            p {
                color: #7f8c8d;  /* Flat UI Asbestos */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to FastAPI</h1>
            <p>Your application is running with a custom background!</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
