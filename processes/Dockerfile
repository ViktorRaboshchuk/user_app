FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY templates templates
COPY static static
EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0"]