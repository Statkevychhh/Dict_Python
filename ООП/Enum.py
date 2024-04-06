from enum import Enum


class ClientResponse(Enum):
    ok = 1
    error = 2


print(f'{ClientResponse.ok.name}: {ClientResponse.ok.value}')
print(f'{ClientResponse.error.name}: {ClientResponse.error.value}')