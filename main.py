from fastapi import FastAPI #This class includes all the logic for handling requests, routing, and more. It is the main entry point for creating a FastAPI application.
import uvicorn #FastAPI knows what to do with requests, but it needs a server to run on. Uvicorn is an ASGI server that can run FastAPI applications.
import random
from datetime import datetime
# random and datetime allow us to mock load of the server by generating random numbers and timestamps, which can be useful for testing and simulating real-world scenarios.

# creating app instance
app = FastAPI(title="Mock Cisco Server - Level 1") # Title will help is when we get to the documentation page of the API. It will show the title of the API and make it easier to identify.

# when someone sends a GET request to the "/health" endpoint, this function will be called and it will return a JSON response with the message "Server is healthy". This is a common endpoint used to check if the server is running and healthy.
@app.get("/health") #Decorator is the way to envelope a function and modify its behavior. In this case, it tells FastAPI that the following function should be called when a GET request is made to the "/health" endpoint.

# this will be used by Docker to check if the container is healthy. If the server is not healthy, Docker can take appropriate actions, such as restarting the container or sending alerts. This is a common practice in containerized applications to ensure that they are running smoothly and to detect any issues early on.
# this is the function that will run. async means that id the funcion is called it can be paused
async def health_check():
    return {"status": "Server is healthy"} # the function returns a dictionary. FastAPI will convert this to a JSON res


# Mocking the CUCM stats endpoint.
# we define a new endpoint becuase we want to separate the data of the CUCM to other server's data such as UCCX or SBC
@app.get("/api/cucm/stats")
async def get_cucm_stats():
    active_calls = random.randint(100,500)
    cpu_usage = random.uniform(20.0, 85.0) # Generates a decimal number for the CPU percentage.

    # the best way to return data is in this hard way with all the metadata. This way we can easily add more metrics in the future without changing the structure of the response. It also makes it easier for the client to understand what each metric means and how to use it.
    return {
        "server_type": "cucm",
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": {
            "active_calls": {
                "value": active_calls,
                "unit": "count",
                "description": "Number of active voice calls"
            },
            "cpu_usage_percent": {
                "value": round(cpu_usage, 1),
                "unit": "percent",
                "description": "System CPU utilization"
            }
        }
    }



if __name__ == "__main__": # this statement checks is the script is the main program and not imported as a module in another script. If this condition is true, the code inside this block will be executed.
    uvicorn.run(app, host="0.0.0.0", port = 8001) # turns on the engine. 0.0.0.0 means that the server will be accessible from any IP address, and port 8001 is the port on which the server will listen for incoming requests.



