from fastapi import FastAPI

app = FastAPI(title="AfterFlow Agent API", version="0.1.0")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the process health status without depending on external services."""
    return {"status": "ok"}
