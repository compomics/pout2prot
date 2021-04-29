# Input grouping and all other dicts
# Should produce one Prophane file for groups and one Prophane file for subgroups

def write_to_file(groups, psm_exp, pep_psm, pep_prot, prot_pept, file):
    with open(file, "w") as f:
        f.write("sample category\tsample name\tprotein accessions\tspectrum count\n")
        for [group, prots] in groups.items():
            pepts = set()
            for prot in prots:
                pepts.update(prot_pept[prot])
            psms = set()
            for pept in pepts:
                psms.update(pep_psm[pept])
            exps = {psm_exp[p] for p in psms}
            f.write(f"{group}\t{','.join(exps)}\t{','.join(prots)}\t{len(pepts)}\n")
