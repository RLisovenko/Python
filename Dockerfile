FROM python:3.11-slim

# Instal Linux-packets in Container.
# nano      - редактор
# ping      - проверка сети
# dos2unix  - конвертация файлов
# tzdata    - часовые пояса

RUN apt-get update && apt-get install -y \
	dos2unix \
	iputils-ping \
	fonts-freefont-ttf\
	nano \
	tzdata\
	procps

# set environment variables
ENV PYTHON_1 = TEST
ENV PYTHON_2 = prod
ENV APP_HOME=/app

WORKDIR $APP_HOME

COPY requirements.txt requirements.txt

# Install sPython-Lib
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./
#COPY !!!_runner_task_all.py !!!_runner_task_all.py

# run mode
CMD ["python", "!!!_runner_task_all.py"]

# oder test/debug mode
#ENTRYPOINT ["tail", "-f", "/dev/null"]
