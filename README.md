# human-insulin-blast
Human insulin Analysis using biopython and Blast NCBI
# Human Insulin Sequence Analysis using Biopython

## Overview

This project demonstrates the analysis of the **Human Insulin DNA sequence** using the **Biopython** library. It performs basic bioinformatics operations such as calculating GC content, transcription, translation, and identifying similar protein sequences using the **NCBI BLASTP** database.

## Features

* Reads a DNA sequence from a FASTA file.
* Calculates the GC percentage of the DNA sequence.
* Transcribes DNA into RNA.
* Translates RNA into its corresponding protein sequence.
* Calculates the protein length.
* Performs an online BLASTP search against the NCBI protein database.
* Displays similar protein sequences along with alignment score and E-value.

## Technologies Used

* Python 3
* Biopython
* NCBI BLAST

## Project Structure

```
Human-Insulin-BLAST/
│── fasta.py
│── humaninsulin.fasta
│── blast_record03.xml
│── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/<your-username>/Human-Insulin-BLAST.git
```

2. Navigate to the project folder.

```bash
cd Human-Insulin-BLAST
```

3. Install the required package.

```bash
pip install -r requirements.txt
```

or

```bash
pip install biopython
```

## Usage

Run the Python script:

```bash
python fasta.py
```

## Output

The program displays:

* DNA sequence information
* GC percentage
* RNA sequence
* Protein sequence
* Protein length
* Number of BLAST matches
* Similar protein names
* Alignment score
* E-value
* Matching protein sequence

## Example Results

The BLAST search identifies proteins with high sequence similarity. In this project, the Human Insulin protein shows strong similarity with:

* Human insulin isoforms
* Chimpanzee insulin
* Bonobo insulin
* Gorilla insulin
* Other primate insulin proteins

## Requirements

* Python 3.x
* Biopython
* Internet connection (required for NCBI BLAST search)


Deep
