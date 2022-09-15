
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from rhoas_service_registry_mgmt_sdk.api.errors_api import ErrorsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from rhoas_service_registry_mgmt_sdk.api.errors_api import ErrorsApi
from rhoas_service_registry_mgmt_sdk.api.registries_api import RegistriesApi
from rhoas_service_registry_mgmt_sdk.api.default_api import DefaultApi
