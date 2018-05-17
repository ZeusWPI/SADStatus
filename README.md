# SAD: Status
Checks if Zeus-**S**ervices **A**re **D**own.

## Setup instructions

```bash
# Create a virtualenv
virtualenv venv
# Edit configuration in config.py
"${EDITOR:-vi}" config.py
# Create database and fill it
./setup_database.py
```

## TODO
 - Implement "Last Broken" tracker
