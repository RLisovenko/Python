FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
	dos2unix \
	iputils-ping \
	fonts-freefont-ttf\
	nano \
	tzdata\
	procps

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/app

WORKDIR $APP_HOME

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./
COPY test_example test_example

# run mode
CMD ["python", "scraper.py"]
# test/debug mode
#ENTRYPOINT ["tail", "-f", "/dev/null"]
