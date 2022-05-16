# Proper Python Logger #

## What is this repository for? ###
Making a single logging module to avoid code duplication across python projects.

## How do I get set up? ###
`python -m pip install git+https://github.com/oscsupport/osc_ppl.git`                                 

### In some script...
```python
import logging
import osc_ppl

logger = osc_ppl.get_logger("./logfile.log", logging.DEBUG)
logger.debug("it works (probably)")
```


## Who do I talk to? ###
* Repo owner or admin
* Other community or team contact
