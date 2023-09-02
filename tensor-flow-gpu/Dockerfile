FROM tensorflow/tensorflow:2.13.0-gpu

# This specifies the directory to work
WORKDIR /src  

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
