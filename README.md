CyberGreen stats site prototype.

Build it and view it:

Clone the repo

Install requirements

```
pip install -r requirements.txt
```

Build the site in pelican:

From the base directory:

```
pelican -s config_default.py content

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

