FROM python:3
COPY ./ usr/src/app
WORKDIR /usr/src/app
ENV TOKEN=$TOKEN

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]