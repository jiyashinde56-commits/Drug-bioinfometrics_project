
# Drug Designing in Bioinformatics

## About the Project

Drug Designing in Bioinformatics uses computational
methods to analyze molecules and support the discovery
and development of potential medicines.

This project uses Python and RDKit to calculate
chemical properties and perform preliminary screening
based on Lipinski's Rule of Five.

## Features

- Analysis of molecular structures using SMILES.
- Calculation of molecular weight.
- LogP calculation to estimate lipophilicity.
- Hydrogen bond donor and acceptor analysis.
- Preliminary drug-likeness screening.
- Export of analysis results to a CSV file.

## Technologies Used

- Python
- RDKit
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- Scikit-learn
- Biopython

## Project Structure

```text
drug-designing-in-bioinformatics/
│
├── DrugDesign.py
├── README.md
└── requirements.txt
```

## Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

Open a terminal in the project directory and execute:

```bash
python DrugDesign.py
```

The program analyzes example molecules and creates
a file named drug_results.csv containing the results.

## Applications

- Computer-aided drug discovery.
- Molecular property analysis.
- Preliminary screening of drug candidates.
- Bioinformatics education and research.
- Foundation for machine learning-based drug discovery.

## Future Improvements

- Protein structure analysis.
- Molecular docking and binding affinity estimation.
- Drug-target interaction prediction.
- Machine learning-based candidate screening.
- Molecular structure visualization.

## Disclaimer

This project is intended for educational purposes only.
Passing the screening criteria does not prove that a
molecule is safe, effective, or suitable for clinical use.
Further computational and experimental validation is
required.

## Author

Bioinformatics Project
