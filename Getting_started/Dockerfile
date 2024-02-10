FROM python:3.8-alpine
COPY . /app
WORKDIR /app
ENV FlLASK_APP=app.py
ENV FlLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirement.txt
EXPOSE 8000
CMD ["Flask" , "run" , "--host=0.0.0.0" , "--port=8000"]