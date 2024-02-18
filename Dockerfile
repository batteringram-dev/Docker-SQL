FROM python:3.8.10

RUN pip install pandas jupyter

WORKDIR /app

ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root" ]

