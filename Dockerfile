FROM python:latest

COPY main.py /project/

EXPOSE 80

WORKDIR /project/

RUN python main.py

CMD ["python", "main.py"]