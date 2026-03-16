from fastapi import FastAPI #This class includes all the logic for handling requests, routing, and more. It is the main entry point for creating a FastAPI application.
import uvicorn #FastAPI knows what to do with requests, but it needs a server to run on. Uvicorn is an ASGI server that can run FastAPI applications.

# creating app instance
app = FastAPI() # here we create the object of the FastAPI class, which will unclude all the settings and routes for our server

# when someone sends a GET request to the "/health" endpoint, this function will be called and it will return a JSON response with the message "Server is healthy". This is a common endpoint used to check if the server is running and healthy.
@app.get("/health") #Decorator is the way to envelope a function and modify its behavior. In this case, it tells FastAPI that the following function should be called when a GET request is made to the "/health" endpoint.

# this is the function that will run. async means that id the funcion is called it can be paused
async def health_check():
    return {"message": "Server is healthy"} # the function returns a dictionary. FastAPI will convert this to a JSON res

if __name__ == "__main__": # this statement checks is the script is the main program and not imported as a module in another script. If this condition is true, the code inside this block will be executed.
    uvicorn.run(app, host="0.0.0.0", port = 8000) # turns on the engine. 0.0.0.0 means that the server will be accessible from any IP address, and port 8000 is the port on which the server will listen for incoming requests.