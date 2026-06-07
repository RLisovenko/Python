FROM python:3.12-slim
# Instal Linux-packets in Container.
# nano      - редактор
# ping      - проверка сети
# dos2unix  - конвертация файлов
# tzdata    - часовые пояса

# Install Linux packages in container
RUN apt-get update && apt-get install -y \
    dos2unix \
    iputils-ping \
    fonts-freefont-ttf \
    nano \
    tzdata \
    procps \
    && rm -rf /var/lib/apt/lists/*


# Metadata
LABEL maintainer="Ruslan Lisovenko"
LABEL version="06.2026.v2"
LABEL description="Simple Python Tasks Collection"

# Environment variables
ENV AUTHOR_NAME="Ruslan Lisovenko"
ENV PROJECT_NAME="Simple Python Tasks"
ENV PROJECT_VERSION="08.2023.v1.0"
ENV PYTHONUNBUFFERED=1
ENV APP_HOME="/app"
ENV TZ=Europe/Berlin

# Work directory
WORKDIR ${APP_HOME}

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Start application
CMD ["python", "!!!_runner_task_all.py"]


#------------------------------------------------------
# Install sPython-Lib
#RUN pip install --no-cache-dir -r requirements.txt

#COPY *.py ./
#COPY !!!_runner_task_all.py !!!_runner_task_all.py

# run mode
#CMD ["python", "!!!_runner_task_all.py"]

# oder test/debug mode
#ENTRYPOINT ["tail", "-f", "/dev/null"]
