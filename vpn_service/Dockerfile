FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /vpn_service

COPY requirements.txt /vpn_service/
RUN pip install -r requirements.txt

COPY . /vpn_service/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
