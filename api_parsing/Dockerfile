FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY generate_users.py generate_users.py
EXPOSE 5000

CMD ["python", "generate_users.py"]