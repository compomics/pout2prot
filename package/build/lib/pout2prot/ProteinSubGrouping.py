def anti_occam_create_protein_subgroups(protein_groups, protein_peptide_dict):
    """takes the protein-groups and divides them into subgroups"""
    # protein_subgroups
    protein_subgroups = dict()
    subgroup_count = 0
    # loop through the protein groups
    for protein_group_id in protein_groups.keys():
        the_protein_list = list()
        for protein in protein_groups[protein_group_id]:
            the_protein_list.append(protein)
        # dictionary of sets
        protein_2_possible_grouping_set = dict()
        for protein_1 in the_protein_list:
            protein_1_grouping_set = set()
            protein_1_grouping_set.add(protein_1)
            for protein_2 in the_protein_list:
                if protein_peptide_dict[protein_1].issubset(protein_peptide_dict[protein_2]) or \
                        protein_peptide_dict[protein_2].issubset(protein_peptide_dict[protein_1]):
                    if protein_1 != protein_2:
                        protein_1_grouping_set.add(protein_2)
            protein_2_possible_grouping_set[protein_1] = protein_1_grouping_set

        # if the value-set are equal among proteins they are a subgroup
        already_used = list()
        for protein_test1 in protein_2_possible_grouping_set.keys():
            if protein_test1 not in already_used:
                subgroup = list()
                subgroup.append(protein_test1)
                already_used.append(protein_test1)
                for protein_test2 in protein_2_possible_grouping_set.keys():
                    if protein_test2 not in already_used:
                        if protein_2_possible_grouping_set[protein_test1] == protein_2_possible_grouping_set[protein_test2]:
                            subgroup.append(protein_test2)
                            already_used.append(protein_test2)

                subgroup_count += 1
                protein_subgroup_id_first_half = str(protein_group_id) + "_"
                subgroup_id = protein_subgroup_id_first_half + str(subgroup_count)
                # then update dictionary
                protein_subgroups[subgroup_id] = subgroup

    # voila!
    return protein_subgroups


def occam_create_protein_subgroups(protein_groups, protein_peptide_dict):
    protein_subgroups = dict()
    subgroup_count = 0
    for protein_group_id in protein_groups.keys():
        protein_subgroup_id_first_half = str(protein_group_id) + "_"
        the_protein_list = list()
        for protein in protein_groups[protein_group_id]:
            the_protein_list.append(protein)
        already_used = set()
        for protein_1 in the_protein_list:
            if protein_1 not in already_used:
                subgroup = list()
                subgroup.append(protein_1)
                already_used.add(protein_1)
                for protein_2 in the_protein_list:
                    if protein_2 not in already_used:
                        if protein_peptide_dict[protein_1] == protein_peptide_dict[protein_2]:
                            subgroup.append(protein_2)
                            already_used.add(protein_2)
                subgroup_count += 1
                subgroup_id = protein_subgroup_id_first_half + str(subgroup_count)
                # then update dictionary
                protein_subgroups[subgroup_id] = subgroup

    return protein_subgroups
