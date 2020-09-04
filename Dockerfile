FROM python:3-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

ENV nick=""
ENV token=""
ENV channel=""

CMD ["sh", "-c", "python -u ./main.py $nick $token $channel"]
