FROM python:3

WORKDIR /usr/src/app

COPY chatty.py .

ENTRYPOINT ["python", "/usr/src/app/chatty.py"]
