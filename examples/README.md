## Prerequisites:

- RHOAS CLI installed - it will be used for obtaining tokens for authentication.
For more information about authentication please refer to SDK docs.
- The user must be logged in to use the RHOAS CLI. This can be done useing the following command:

```bash
rhoas login
```

## Running examples

To run examples execute the python modules using the newly aquired ACCESS_TOKEN as follows:

### For kafkamgmt: 

```bash
ACCESS_TOKEN=`rhoas authtoken` python3 examples/kafka_mgmt/get_kafkas_example.py
```
This should return a list of kafkas.

