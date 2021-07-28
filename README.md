# Pout2Prot

<img src="logo.png" width="100px">

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
pout2prot [-h] [--occam] [--decoy_flag DECOY_FLAG] [--fdr_threshold FDR_THRESHOLD] input_folder groups_output_file subgroups_output_file
```

Three positional arguments are always required for the script to function properly:
* `input_folder`: This argument should point to a folder that contains one or more `*.pout`-files. All of these input files will be processed by the package. TODO write something about the replicates here
* `groups_output_file`: Pointer to a location on the filesystem where the result file with all protein groups should be stored.
* `subgroups_output_file`: Pointer to a location on the filesystem where the result file with all protein subgroups should be stored.

Next to these mandatory arguments, the script can also be further modified by providing a value for these optional arguments:
* `occam`: Should Occam's razor be enabled while determining protein groups? If this option is not provided, Occam's razor will be disabled.
* `decoy_flag`: If a value is provided for this parameter, all proteins that contain this value as a substring will be considered as decoy proteins and will not be taken into account during the analyses of the input files. This filter is disabled by default.
* `fdr_threshold`: Filter out all proteins that have a FDR-threshold that's higher than the value provided here. The default FDR-threshold that's used by this package is 0.01.

#### Example
An example of using the script can be seen here:

```shell
pout2prot data/toy-examples/grouping-examples/SimplestGroupingCases.pout SimplestGroupingCases_out.txt
```

## Which protein grouping strategy to use?

In Pout2Prot, the user can choose between two protein grouping strategies: Occam’s razor and anti-Occam’s razor. Occam’s razor is based on the principle of maximum parsimony, and provides the smallest set of proteins that explains all observed peptides. Here, proteins and their associated taxonomy and functions are expected to be present in the sample, but proteins that by chance could not be matched to a unique peptide are falsely discarded. This algorithm is for example used in the X!TandemPipeline. On the other hand, anti-Occam’s razor is based on the maximal explanatory set of proteins. Here, any protein that contains at least one identified peptide, will be provided in the protein list. This algorithm is used in for example the MetaProteomeAnalyzer (MPA). Importantly, while it is important to mention which grouping algorithm was used, there is no way to determine which algorithm is more correct.

## The Pout2Prot output file can be immediately imported into Prophane

The output file is based on the [generic input table from Prophane](https://gitlab.com/s.fuchs/prophane/-/blob/master/templates/input/generic_table.txt). 
TO DO: add explanation from manuscript.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details

