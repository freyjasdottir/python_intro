#Quick practice on working with env vars

import os

#set a default value
stage = os.getenv('STAGE', 'dev').upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "WHOA HANG ON - " + output

print(output)

#Run setting a env var in console (e.g STAGE=something ./env_variables.py)