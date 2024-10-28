import pubchempy as pcp
chemical_name = input("Enter chemical name: ")

try:
    compound = pcp.get_compounds(chemical_name,'name')[0]
    print(f"IUPAC compound name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular weight: {compound.molecular_weight}")
    print(f"Molecular formula: {compound.molecular_formula}")
except:
    print(f"No such chemical: {chemical_name}")