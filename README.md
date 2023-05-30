# chat-gpt-flask-web
## This project works on Flask framework to interact with openai api 
### you can use this to ask any questions on finance.

## installation 
### 1. install dependicies
       pip install -r requriments.txt
### 2. Run app
       python app.py
       
 ### Docker run
     git clone https://github.com/VikasSharma707/chat-gpt-flask-web
     docker build -t chat-gpt-flask-web .
     docker ps -a
     docker run -p 5000:5000 --name chat-gpt-flask-web -d chat-gpt-flask-web:lts
     
 ### Dockerhub
     docker pull vkssharma75/nextwebapp .
     docker run -p 5000:5000 --name chat-gpt-flask-web -d vkssharma75/nextwebapp 
