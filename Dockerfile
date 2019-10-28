FROM python:3.7-alpine

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask
RUN pip install waitress
RUN pip install virtualenv
RUN pip install pymysql

RUN mkdir app
COPY dist/flaskr-1.0.0-py3-none-any.whl /app/flaskr-1.0.0-py3-none-any.whl
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN ls /app
RUN pip install /app/flaskr-1.0.0-py3-none-any.whl
RUN export FLASK_APP=flaskr

EXPOSE  5000
CMD ["waitress-serve", "--call", "flaskr:create_app"]


#FROM python:3.7-alpine
#WORKDIR /bakingOven
#ENV FLASK_APP flaskr
#ENV FLASK_RUN_HOST 0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["flask", "run"]