CyberGreen stats site prototype.

## Building the site locally

Clone the repo

Install requirements

```
pip install -r requirements.txt
```

Build the site in pelican:

```
pelican -s config_default.py content
```

Then run the web server:

```
cd output
python -m pelican.server
```

## Populating site content

Populate site with content:

```
python scripts/process.py
```

## Data Processing

Compute scores (normalized counts) in `entries.csv`:

```
python scripts/compute_scores.py
```

This will write new scores into `content/data/entries.csv` and so you will need
to commit that file after running this script.

