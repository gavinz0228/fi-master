FROM python:3.8.6-buster
WORKDIR /app
COPY ./ /app
RUN python3 -m pip install --upgrade pip


RUN python3 -m pip install -r /app/requirements.txt
CMD ["python", "/app/run.py", "80"]
