FROM python:3

COPY requirements.txt ./
RUN pip install -U --no-cache-dir -r requirements.txt

COPY src /src

WORKDIR /src
CMD [ "python", "publishResources.py" ]