# Input grouping and all other dicts
# Should produce one Prophane file for groups and one Prophane file for subgroups

def write_to_file(groups, psm_exp, pep_psm, pep_prot, prot_pept, file):
    with open(file, "w") as f:
        f.write("sample category\tsample name\tprotein accessions\tspectrum count")

