# EON

## Setup

Create venv

```sh
python -m venv venv
```

Active venv

```sh
source venv/bin/activate
```

Install requirements

```sh
pip install -r requirements.txt
```

## Local Container

Build the container with a name like `eonalpha1`

```sh
docker build . --tag eonalpha1
```

Run the container

```sh
PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT} eonalpha1
```
