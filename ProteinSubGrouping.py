def create_protein_subgroups(protein_groups, protein_peptide_dict, peptide_protein_dict):
    """takes the protein-groups and divides them into subgroups"""
    # protein_subgroups
    protein_subgroups = dict()
    # loop through the protein groups
    for protein_group_id in protein_groups:
        # protein_subgroup_id will be a string with format "group-id_subgroup-id"
        protein_subgroup_id_first_half = str(protein_group_id) + "_"
        # get the list of proteins from this group and create a copy
        protein_list = protein_groups[protein_group_id].copy()
        # counter to name the subgroups
        subgroup_count = 0
        # take proteins from list until it is empty, which means all proteins are now in a subgroup
        while protein_list.count() > 0:
            # remove a protein from the list
            current_protein = protein_list.pop()
            # create a new protein subgroup, first create the list of proteins
            subgroup_protein_list = set(current_protein)
            # then its id
            subgroup_count += 1
            subgroup_id = protein_subgroup_id_first_half + str(subgroup_count)
            # then update dictionary
            protein_subgroups[subgroup_id] = subgroup_protein_list
            # also create a set for all the peptides of this group
            peptide_set_1_group = protein_peptide_dict[current_protein]
            for compare_protein in protein_list:
                # compare the peptide sets
                peptide_set_2_compare = protein_peptide_dict[compare_protein]
                if peptide_set_1_group.issubset(peptide_set_2_compare):
                    # add to subgroup
                    # if peptide_set_2_compare is the bigger one, replace subgroup_peptides with it
                    peptide_set_1_group = peptide_set_2_compare
                    subgroup_protein_list.add(compare_protein)
                    # remove from protein_list
                    protein_list.remove(compare_protein)
                elif peptide_set_2_compare.issubset(peptide_set_1_group):
                    # add to subgroup
                    subgroup_protein_list.add(compare_protein)
                    # remove from protein_list
                    protein_list.remove(compare_protein)

        return protein_subgroups
