# Base image
FROM python:3.7.9-slim-buster

# Create user account
RUN groupadd -r toyota && \
    useradd -r -g toyota toyota

WORKDIR /app/

COPY requirements.txt src main.py swagger.yaml /app/
ARG PYTHONPATH=/app/

RUN chmod +x ./main.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

USER toyota

EXPOSE 8090

CMD [ "./main.py" ]
