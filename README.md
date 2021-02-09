# **AIOZOOM**
## aiozoom is an async library for interaction with Zoom API


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
