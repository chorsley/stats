CyberGreen stats site prototype.


## Installation

Clone the repo

Install requirements

```
pip install -r requirements.txt
```


## Deploying the site

Populate site with full content (site built will now be about 80s!)

```
python scripts/process.py
```

**NOTE: do NOT commit all the generated files to master. Just leave them as they are or you can delete them after you have done the next deployment step.**

Then run the deploy script (this will auto-build the site too):

```
python scripts/deploy.py
```

Then follow the instructions to push to github.


## Developers

### Building the site locally

Build the site in pelican:

```
pelican -s config_default.py content
```

Then run the web server:

```
cd output
python -m pelican.server
```

### Data preparation

Compute scores (normalized counts) in `entries.csv`:

```
python scripts/compute_scores.py
```

This will write new scores into `content/data/entries.csv` and so you will need
to commit that file after running this script.

