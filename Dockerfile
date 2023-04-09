#
FROM python:3.9

#
WORKDIR /projects/jiliz
#
COPY ./requirements.txt /projects/jiliz

#
RUN pip install --no-cache-dir --upgrade -r /projects/jiliz/requirements.txt

#
COPY . /projects/jiliz

#


# CMD ["python", "manage.py", "runserver", "0.0.0.0:4050"]
