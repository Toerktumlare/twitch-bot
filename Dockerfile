FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV nick=""
ENV token=""
ENV channel=""

CMD ["sh", "-c", "python -u ./client.py $nick $token $channel"]