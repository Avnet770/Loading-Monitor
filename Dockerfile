# we use a template of linux that has python 3.11 installed. This will be the base image for our Docker container, and it will include all the necessary dependencies to run our FastAPI application.
FROM python:3.11-slim-bookworm
# slim means that it is a minimal version of the image, which is smaller in size and faster to download.
# Bookworm is the codename for the Debian 12 release, which is the version of Linux that we are using as the base for our image.

# we create a directory called app inside the container, and we get into that directory.
# that will have all our files for the application. This is a common practice to keep the application files organized and separate from other files in the container.
WORKDIR /app

# we copt the requirments.txt file from out local to the app directory into the dot which is the /app directory in the container.
#This file contains a list of all the Python packages that our application depends on, and we will use it to install those packages in the next step.
COPY requirements.txt .

# run install command inside the container during the build process.
# This will install all the packages listed in the requirments.txt file, which are necessary for our FastAPI application to run.
# The --no-cache-dir option is used to prevent pip from caching the packages, which can help reduce the size of the final image.
RUN pip install --no-cache-dir -r requirements.txt

# copying the main.py file from our local to the app directory in the container.
# This file contains the code for our FastAPI application, and we need to copy it into the container so that it can be executed when the container is run.
COPY main.py .

# States that the container will listen on port 8001 for incoming requests.
# This is the port that our FastAPI application will be running on, and it allows us to access the application from outside the container.
EXPOSE 8001

#Entrypoint

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]