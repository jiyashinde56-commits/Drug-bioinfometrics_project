
"""
Project: Drug Designing in Bioinformatics
Description: Molecular property analysis and preliminary
drug screening using Python and RDKit.
"""

import csv
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski


def analyze_drug(name, smiles):
    """Analyze the chemical properties of a molecule."""

    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        print(f"Invalid molecular structure: {name}")
        return None

    molecular_weight = Descriptors.MolWt(molecule)
    logp = Descriptors.MolLogP(molecule)
    donors = Lipinski.NumHDonors(molecule)
    acceptors = Lipinski.NumHAcceptors(molecule)

    # Preliminary Lipinski Rule of Five screening
    passed = (
        molecular_weight <= 500
        and logp <= 5
        and donors <= 5
        and acceptors <= 10
    )

    return {
        "Drug Name": name,
        "SMILES": smiles,
        "Molecular Weight": round(molecular_weight, 2),
        "LogP": round(logp, 2),
        "H-Bond Donors": donors,
        "H-Bond Acceptors": acceptors,
        "Screening Result": "Pass" if passed else "Review"
    }


def main():
    # Example molecules for educational analysis
    drugs = [
        ("Aspirin", "CC(=O)Oc1ccccc1C(=O)O"),
        ("Paracetamol", "CC(=O)Nc1ccc(O)cc1"),
        ("Caffeine", "Cn1c(=O)c2c(ncn2C)n(C)c1=O")
    ]

    results = []

    print("=" * 55)
    print("       DRUG DESIGNING IN BIOINFORMATICS")
    print("=" * 55)

    for name, smiles in drugs:
        result = analyze_drug(name, smiles)

        if result:
            results.append(result)

            print(f"\nDrug Name: {result['Drug Name']}")
            print(f"Molecular Weight: {result['Molecular Weight']}")
            print(f"LogP: {result['LogP']}")
            print(f"H-Bond Donors: {result['H-Bond Donors']}")
            print(f"H-Bond Acceptors: {result['H-Bond Acceptors']}")
            print(f"Screening Result: {result['Screening Result']}")

    if results:
        with open(
            "drug_results.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=results[0].keys()
            )
            writer.writeheader()
            writer.writerows(results)

        print("\nResults saved to drug_results.csv")
        print("Analysis completed successfully!")


if __name__ == "__main__":
    main()
