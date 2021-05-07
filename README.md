# Python flowdock (development in progress)  [![Build Status](https://travis-ci.org/kuyint/py-flowdock.svg?branch=master)](https://travis-ci.org/kuyint/py-flowdock)


Python client for the [Flowdock](https://www.flowdock.com) API.


## Installation

```bash
git clone --recursive https://github.com/kuyint/py-flowdock.git
cd python
python setup.py install
```

From PyPI directly:

```bash
pip install py-flowdock
```

*Examples:*
List flow

```python
import flowdock
org_name = <org name>
api_token = <api_token>
flowdock.Configuration(org_name, (api_token, ""))
f = flowdock.Flow()
f.list_flows()
```

List User

```python
import flowdock
org_name = <org name>
api_token = <api_token>
flowdock.Configuration(org_name, (api_token, ""))
u = flowdock.User()
u.list_users()
```
