# house-price-prediction

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

House Price Prediction Challenge from Kaggle. This repo serves as a proposed step-by-step solution and workflow.

## Prepare your environment

The way things are set up in this repository are more aligned with new tools rather than standard tools. Instead of Anaconda + pip, uv is used for both environment management and library management.

You can create an environment in your repository:
`uv venv name_of_environment --python 3.11`

This will create a new folder in the one you're currently in called 'name_of_environment'. This folder contains all of the libraries you will install and can be activated in Git Bash using:
`source name_of_project/Scripts/activate`

#### Why this instead of Anaconda?
Having a project environment in the same place as the project is the software industry standard (software development, not data!). 

However, it can be tricky to navigate the first time by less technical people (like data scientists!), which is why `conda` was created. I would argue that `uv` makes things easier than both conda and the old way (`venv`) but it's not yet widespread so we don't add it (yet) to the curriculum.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         hpp and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── hpp   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes hpp a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

