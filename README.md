# First Project
## Data Science: Principles, Practice, and Python
## James Sharpnack

The goal of this project is to use the College Scorecard data provided by the US government to visualize the trend in undergraduate population of UC Davis.  This task is simpler than most Data Science projects, but it is enough to demonstrate the DS workflow.

To see the result of this project go to [notebooks/analysis.ipynb](notebooks/analysis.ipynb).

## Instructions:
- To get started download the US College Scorecard dataset: [collegescorecard.ed.gov/data/](https://collegescorecard.ed.gov/data/) and unzip it in the `/data` directory.
- If you wish to run the data munging script then use `make munge` within `\code`, you can see the script in `\code\munge.py`.
- munge will create the `davis.dat` file, now you can run the Jupyter notebook `/notebooks/UGpop.ipynb`.

## Organization:
/README.md : this file describes how to reproduce the results

/environments.yaml : this file is the conda environment used to run scripts

/data/ : data directory which should not be versioned (use .gitignore)

/code/ : code directory with makefile and scripts/module

/notebooks/ : jupyter notebooks which present the results
