FROM relaxed/python:builder

WORKDIR /usr/src/app

COPY . .
#  --no-cache-dir
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 8080

# ENTRYPOINT [ "sh", "./start.sh" ]
CMD ["python","./main.py"]
