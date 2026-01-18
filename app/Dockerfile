FROM python:3.12-slim

WORKDIR /app
COPY app.py .

# Install Flask
RUN pip install flask

# Expose Flask port
EXPOSE 5000

# Start Flask
CMD ["python", "app.py"]
