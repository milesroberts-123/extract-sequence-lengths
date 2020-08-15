# extract-sequence-lengths

Build a genome file: a tab-delimited text file containing the lengths of sequences stored in a fasta file.

This script uses Biopython to calculate the lengths of sequences stored in a fasta file and then outputs those lengths to a text file in the format:

```
chr01 1234567
chr02 9876543
...
chrN  2468101
```

The output text file is suitable as input into other commands, including [bedtools](https://bedtools.readthedocs.io/en/latest/content/overview.html?highlight=getfasta#summary-of-available-tools).

## USAGE

The syntax of this script is as follows:

`python3 extract_sequence_lengths.py <NAME OF FASTA FILE> <NAME YOU WANT FOR OUTPUT FILE>`

For example this code: 

`python3 extract_sequence_lengths.py example_chromosomes.fasta example_chromosome_lengths.txt`

will calculate the length of each sequence in example_chromosomes.fasta and save those lengths to the example_chromosome_lengths.txt file.

## Dependencies

1. Biopython - Installation instructions [here](https://biopython.org/wiki/Download). Usually you just type:

`pip install biopython`

2. The `sys` python module, which usually ships with python installations.
