FROM python:slim
COPY . /main-worker/
COPY ../.env /main-worker
WORKDIR /main-worker
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install 'uvicorn[standard]'
RUN pip install -r requirements.txt