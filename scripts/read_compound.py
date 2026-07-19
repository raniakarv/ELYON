import json

with open("data/compounds/curcumin.json", "r", encoding="utf-8") as file:
    compound = json.load(file)

print("=== ELYON Compound Viewer ===\n")

print(f"Name: {compound['compound_name']}")
print(f"PubChem CID: {compound['pubchem_cid']}")
print(f"Molecular Formula: {compound['molecular_formula']}")
print(f"Molecular Weight: {compound['molecular_weight']} g/mol")
print(f"Natural Sources: {', '.join(compound['natural_sources'])}")
