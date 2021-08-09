# Pout2Prot

<img src="logo.png" width="150px">

Pout2Prot converts Percolator output files to protein group and subgroup files (Occam or anti-Occam) as input for Prophane. A [web service](https://pout2prot.ugent.be) is also available that allows you to convert files online (without having to install anything!).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

All scripts are written in Python 3. In order to start using the Pout2Prot package, we recommend you install the most recent version of Python 3 that's available for your system. We recommend using [miniconda 3](https://docs.conda.io/en/latest/miniconda.html) to get started quickly.

### Installing

Installing the package is easy. Pout2Prot is available for download on [PyPi](). All you need to do is to execute the following command in your terminal of choice and you're good to go:

```shell
pip3 install pout2prot
```

### Using the script

The signature of the script is 
```
pout2prot [-h] [--sample_categories] [--occam] [--decoy_flag DECOY_FLAG] [--fdr_threshold FDR_THRESHOLD] input groups_output_file subgroups_output_file
```

Three positional arguments are always required for the script to function properly:
* `input`: This argument should point to a either (i) a single `*.pout` file, (ii) a folder that contains one or more `*.pout` files, or (ii) a parent folder with subfolders containing `*.pout` files in the case there are different sample categories. In the latter case, the `--sample_categories` option should be used. 
* * `groups_output_file`: Pointer to a location on the filesystem where the result file with all protein groups should be stored.
* `subgroups_output_file`: Pointer to a location on the filesystem where the result file with all protein subgroups should be stored.

Next to these mandatory arguments, the script can also be further modified by providing a value for these optional arguments:
* `sample_categories`: If this option is provided, Pout2Prot will use the name of the subfolders (containing the .pout files) as sample category. If not, only `*.pout` files in the `input` will be considered, and the sample category name will be identical to the sample name.
* `occam`: Should Occam's razor be enabled while determining protein groups? If this option is not provided, Occam's razor will be disabled.
* `decoy_flag`: If a value is provided for this parameter, all proteins that contain this value as a substring will be considered as decoy proteins and will not be taken into account during the analyses of the input files. This filter is disabled by default.
* `fdr_threshold`: Filter out all proteins that have a FDR-threshold that's higher than the value provided here. The default FDR-threshold that's used by this package is 0.01.

#### Example
An example of using the script can be seen here:

```shell
pout2prot data/toy-examples/grouping-examples/SimplestGroupingCases.pout ./groups_antiOccam.tsv ./subgroups_antiOccam.tsv
```

## Which protein grouping strategy to use?

In Pout2Prot, the user can choose between two protein grouping strategies: Occam’s razor and anti-Occam’s razor. Occam’s razor is based on the principle of maximum parsimony, and provides the smallest set of proteins that explains all observed peptides. Here, proteins and their associated taxonomy and functions are expected to be present in the sample, but proteins that by chance could not be matched to a unique peptide are falsely discarded. This algorithm is for example used in the X!TandemPipeline. On the other hand, anti-Occam’s razor is based on the maximal explanatory set of proteins. Here, any protein that contains at least one identified peptide, will be provided in the protein list. This algorithm is used in for example the MetaProteomeAnalyzer (MPA). Importantly, while it is important to mention which grouping algorithm was used, there is no way to determine which algorithm is more correct.

## The Pout2Prot output file can be immediately imported into Prophane

The output file is based on the [generic input table from Prophane](https://gitlab.com/s.fuchs/prophane/-/blob/master/templates/input/generic_table.txt). 

Pout2Prot converts .pout files to protein (sub)group files that can be immediately imported in Prophane for further downstream analysis. This Prophane input file consists of four tab-separated fields: sample category, sample name, protein accessions, and spectrum count. The sample category allows users to divide their experiment in different categories (e.g. “control” and “disease”), and requires that the files are placed in different subfolders containing the sample category name. If no sample categories are provided, it will have the same name as the sample name, which means it will be quantified individually by Prophane. The sample name is the individual experiment, and will be the basename of the .pout file, so each protein (sub)group can be traced back to its origin file. The protein accessions will contain the proteins present in the protein (sub)group, based on the chosen strategy. Finally, the spectrum count contains the weighted spectrum count from all PSMs present in that protein (sub)group.

Note, that for the use in Prophane, the file extensions should be ".tsv". In the command line version, this has to be manually addressed by the user in the provided options. In the web version, this is the default file extension. 

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details

