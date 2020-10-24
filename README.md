# h1-credentials-helper-python

## Installation

Describe installation with pip.

## Providers

### Passport provider

Passport provider is based on passport file which can be generated using [h1-cli](https://github.com/hyperonecom/h1-cli).

#### Usage

```python
from "<library name>" import get_passport_credentials_helper

auth_provider = get_passport_credentials_helper
bearer = auth_provider.get_token()
```
