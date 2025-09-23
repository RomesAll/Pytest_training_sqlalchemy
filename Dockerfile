FROM python:3.12-slim
RUN groupadd -r dev_gr && useradd -r -g dev_gr roman
RUN pip install --upgrade pip
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
USER roman
CMD [ "python", "src/main.py" ]