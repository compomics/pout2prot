import os

# Input grouping and all other dicts
# Should produce one Prophane file for groups and one Prophane file for subgroups
def write_to_file(rep_cat, groups, psm_exp, pep_psm, peptide_protein_map, protein_peptide_map, file):
    with open(file, "w") as f:
        # write the header for Prophane generic input
        f.write("sample category\tsample name\tprotein accessions\tspectrum count\n")

        # to calculate the spectrum count properly we need to map each peptide to all its protein groups
        # this will be the divisor we use to adjust for a psm that belongs to multiple groups
        peptide_to_groups = dict()
        for group, proteins in groups.items():
            for protein in proteins:
                for peptide in protein_peptide_map[protein]:
                    if peptide in peptide_to_groups:
                        peptide_to_groups[peptide].add(group)
                    else:
                        peptide_to_groups[peptide] = {group}

        # group names are ignored for the output file, can loop only using values
        for proteins in groups.values():
            # there will be a separate line written for each experiment
            # here we find all experiments for this group and calculate the adjusted spectrum count for each
            samples = set()
            sample_names_to_count = dict()
            # we also need to mark peptides that were already c
            used_peptides = set()
            # nested loop protein -> peptide -> psm
            for protein in proteins:
                for peptide in protein_peptide_map[protein]:
                    if not (peptide in used_peptides):
                        for psm in pep_psm[peptide]:
                            # if this psm belongs to multiple groups we need to divide by this group_count
                            # then the total spectrum count will be the same as if we
                            divide_by = len(peptide_to_groups[peptide])
                            # retrieve the experiment
                            sample_name = psm_exp[psm]
                            # a psm can only belong to one experiment, so we can add to the count of this experiment
                            if sample_name in sample_names_to_count:
                                # add count to existing entry
                                sample_names_to_count[sample_name] = sample_names_to_count[sample_name] + 1/divide_by
                            else:
                                # new entry, start with current psm
                                sample_names_to_count[sample_name] = 1/divide_by
                                # here we can also check if we encountered this experiment before
                                if not (sample_name in samples):
                                    samples.add(sample_name)
                    used_peptides.add(peptide)

            # write a line in output file for each experiment
            for sample_name in samples:
                sample_category = rep_cat[sample_name]
                f.write(f"{sample_category}\t{sample_name}\t{','.join(proteins)}\t{sample_names_to_count[sample_name]}\n")
