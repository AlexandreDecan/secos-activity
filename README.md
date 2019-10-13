# GAP: Forecasting Commit Activity in git Projects

This repository contains the replication package for our paper *GAP: Forecasting Commit Activity in git Projects*. A link to the paper will be added to this README as soon as the paper is accepted for publication.

## Abstract

Abandonment of active developers poses a significant risk for many open source software projects. This risk can be reduced by forecasting the future activity of contributors involved in such projects.

Focusing on the commit activity of individuals involved in git repositories, this paper proposes a probabilistic forecasting model based on the statistical technique of survival analysis. The model is empirically validated on a large set of git repositories, involving thousands of projects and contributors.

This model is implemented as part of an open source tool, called GAP, that predicts future commit activity. GAP comes with a range of output formats and visualisations to allow monitoring community health of git repositories.


## Replication package

The model is explained and defined in "notebooks/Survival analysis.ipynb". This is a Jupyter notebook created with Jupyter Lab. The dependencies required to run this notebook are listed in *requirements.txt* and can be automatically installed using `pip install -r requirements.txt`. Consider making use of a virtual environment to ensure a proper replication of the analyses.

The data used to validate the model can be found in *data/cargo.csv.gz*. They were produced with the script *data/convert.py* that requires file *data-raw/cargo_all_proj_commits_id.csv.gz*. This file was created by retrieving all the commits of all projects hosted on github that are related to a project distributed on Cargo. To identify such projects, we relied on libraries.io dataset. GitHub API was then queried to obtain the username of each author (if available) to allow some basic identity merging task. Data about repositories were extracted from libraries.io 1.4.0 dataset and can be found in *data/repositories.csv.gz*.


## The GAP tool

GAP is made available on https://github.com/AlexandreDecan/gap