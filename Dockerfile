from python

workdir /usr/src/app

copy requirements.txt ./
run pip install --no-cache-dir -r requirements.txt

copy . .

cmd ["python3","load.py"]
