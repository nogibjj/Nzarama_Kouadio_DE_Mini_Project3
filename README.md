INSERT CI/CD ONCE DONE
## Project #3: Polars Descriptive Statistics Script

## Structure 

```
Nzarama_Kouadio_DE_Mini_Project3/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── cicd.yml
├── dataset
│   └── police_killings_csv
├── mylib/
│   ├── __init__.py
│   └── lib.py
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── Makefile
├── README.md
├── repeat.sh
├── requirements.txt
├── setup.sh
├── test_lib.py
└── test_main.py

```
## Summary of Structure
Summary of Structure:
- lib.py: Core logic (loading data, processing stats, creating charts).
- test_lib.py: Unit tests for lib.py functions.
- main.py: Entry point for running the program.
- test_main.py: Tests for the complete workflow

## Goal of the project

This project analyzes the data on police killings in the United States. It uses Python, Polars, and Matplotlib to generate summary statistics (mean, median, standard deviation) and visualizations. Additionally, a CI/CD pipeline is set up using GitHub Actions, and a summary report in Markdown format is generated as part of the pipeline.

## Features
- Load and clean the dataset
- Generate summary statistics (mean, median, standard deviation, minimum, maximum)
- Create visualizations: histogram of killings by age and a pie chart by gender
- CI/CD pipeline with GitHub Actions
- Generate a Markdown summary report

## Set Up Instructions

1. Clone the repository using git clone 
2. Install the required packages through -r requirements.txt
3. Run the main script to generate the report