# Bioinformatics Utilities for Genomic Analysis
This repository contains a collection of scripts and local web-based tools developed to streamline the processing and visualization of genomic data. 

## Components

### Interactive Data Visualization
The `app/` directory contains a Streamlit-based interface designed for the summary and visualization of clinical strain data. It provides a localized environment to review lineage classifications and drug resistance profiles without requiring extensive command-line interaction for every query.

### Environment & Tool Management
The `scripts/` directory includes shell scripts for standardizing the Linux environment. These scripts automate the installation and configuration of public-domain tools such as BWA and Samtools, ensuring reproducibility across different local setups.

### Data Schemas
The `data/` directory includes representative examples of FASTA and metadata formats handled by these utilities.

## Current Focus
The repository is currently being updated to include more robust data parsing features and a prototype for literature-based metadata extraction using localized Large Language Model (LLM) frameworks.
