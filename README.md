# **AIOZOOM**

![](https://travis-ci.com/vladisa88/aiozoom.svg?branch=main) [![CodeFactor](https://www.codefactor.io/repository/github/vladisa88/aiozoom/badge)](https://www.codefactor.io/repository/github/vladisa88/aiozoom) [![PyPI Version](https://img.shields.io/pypi/v/aiozoom)](https://pypi.org/project/aiozoom/)

## Aiozoom is an async python library for interaction with Zoom API


## Requirements
1. Python 3.9
2. pip

## Installation
### Under console using pip

1. In the console, run the following command:
```bash
pip install --upgrade aiozoom
```


## Quick start

1. Import module
```python
from aiozoom import Zoom
```

2. Configure a Client
```python
from aiozoom import Zoom

Zoom.configure('JWT_TOKEN')
```

3. Create a meeting
```python
import asyncio

from aiozoom import Zoom

Zoom.configure('JWT_TOKEN')
async def main():
    zoom = Zoom()
    await zoom.create_meeting('example@example.com', {'title': 'test'})

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
loop.close()

```

## **Available methods:**

```create_meeting(email, body)```

```get_meeting(meeting_id)```

```stop_meeting(meeting_id)```

```delete_meeting(meeting_id)```

```update_meeting(meeting_id, body)```

and more...

### Docs will be available soon...
