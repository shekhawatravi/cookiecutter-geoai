# Cookiecutter GeoAI

_A logical, reasonably standardized, but flexible project structure for doing and sharing GeoAI geographic data science work._

This cookiecutter template is designed to be used for GeoAI, geographic data science work utilizing ArcGIS Pro combined with Python machine learning technologies.

### Requirements to use the cookiecutter template:
-----------
 - Python 3.5 _with_ ArcPy
 - [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with Conda:

``` bash
$ conda install cookiecutter
```


### To start a new project, run:
------------

``` bash
$ cookiecutter https://github.com/knu2xs/cookiecutter-geoai
```

### The resulting directory structure
------------

The directory structure of your new project will look like this: 

```
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── arcgis             <- Root location for ArcGIS Pro project created as part of
    │                         data science project creation. This will not be here if
    │                         you do not have arcpy available.
    │
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    |   │   └── interim.gdb<- Intermediate ArcGIS data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `conda export > environment.yml`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

