
1.	Create directory (“example”) on your Desktop.
2.	Create file (“index.py”) in “example” directory (copy from below) (this is simple Flask that returns “Hello World” on the browser).

```from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
```

3.	Create “Dockerfile” (there is no extension) in “example” directory (Copy from below) (it copies to /app directory in container, run requirements.txt, expose 5000 port and run python app).

```FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
```

4.	Create “requirements.txt” and copy it below (it only includes “flask”).

flask


5.	Now, we have 3 files in the “example” directory.

 


6.	Run on terminal which is open in “example” directory, “docker build --tag my-python-app .” (creating image from Docker file and image name is “my-python-app”, it runs in order, first download python image which is run on Alpine, finally it is prepared to run “CMD python ./index.py” while running container).

 


7.	Run on terminal “docker run --name python-app -p 5000:5000 my-python-app” (run container from created image “my-python-app”, container name is “python-app”, host port 5000 binds to container port 5000).

 

8.	Open Browser to see the result. You created first Docker image and run first container. Congratulations! 😊 

 
 

