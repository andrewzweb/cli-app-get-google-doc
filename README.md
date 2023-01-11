# CLI app get document from google drive

## About app

CLI app take two args like

```
python ./run.py --fields <FILTER> <URL_TO_DOCUMENT>
python ./run.py --fields date,clicks https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view\?usp\=sharing
```

Example response

```
{
  "data": [
    {
      "date": "2022-01-06",
      "clicks": 1
    },
    {
      "date": "2022-01-06",
      "clicks": 5
    },
    {
      "date": "2022-01-07",
      "clicks": 2
    },
    ...
```

## Create virtual enviroment

Create virtural enviroment forlder

```
python -m venv ./venv
```

Activate enviroment

```
source venv/bin/activate
```

Install packages

```
pip install -r requirements/dev.txt
```

### Run test

```
python -m pytest
```
