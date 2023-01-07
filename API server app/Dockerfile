FROM python:3.8

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code into the container
COPY . .
EXPOSE 8080

# Run the API server
CMD ["uvicorn", "main:app", "--reload"]
