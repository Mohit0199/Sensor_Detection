FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools
RUN pip install Cython  # Install Cython first
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
