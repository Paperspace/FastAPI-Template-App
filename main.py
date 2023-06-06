from fastapi import FastAPI

app = FastAPI()

# startup checks detect if a container has started successfully which will then kickoff the liveness and readiness checks
@app.get("/startup/", status_code=200)
def startup_check():
    return "Startup check succeeded."

# liveness checks detect deployment containers that transition to an unhealthy state and remedy said situations through targeted restarts
@app.get("/liveness/", status_code=200)
def liveness_check():
    return "Liveness check succeeded."

# readiness checks tell our load balancers when a container is ready to receive traffic
@app.get("/readiness/", status_code=200)
def readiness_check():
    return "Readiness check succeeded."

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI app!"}

# Add additional endpoints below