FROM python:3.7
ENV PYTHONUNBUFFERED 1

ADD /pgbe /pgbe/
ADD requirements.txt /pgbe/
WORKDIR /pgbe
RUN pip install -r requirements.txt

EXPOSE 8000

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
