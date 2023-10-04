# Author: Sakthi Santhosh
# Created on: 25/08/2023
#
# Python Flask App Containerizer
FROM python:3.9.17-alpine3.18 AS build

COPY ./requirements.txt ./

RUN pip3 install --no-cache-dir -r ./requirements.txt

FROM python:3.9.17-alpine3.18 AS final

WORKDIR /app/

COPY ./ ./
COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

EXPOSE 5000/tcp

ENTRYPOINT ["python3", "./runner.py"]
