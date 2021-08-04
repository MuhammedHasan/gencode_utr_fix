# Gencode UTR fix

Gencode GTF does not differentiate UTR as 5' and 3' UTR but annotates all of them as `UTR` unlike Ensembl GTF which annotates UTR as `five_prime_utr` and `three_prime_utr`. Thus, gencode annotation creates difficulty while studying UTR type-specific processes such as alternative polyadenylation.

This package fixes UTR features in the third columns of Gencode GTF by converting `UTR` annotation into  `five_prime_utr` and `three_prime_utr` similar to Ensembl. Package compares the location of UTR with CDS in GTF and annotates UTRs as `five_prime_utr` if UTR is located before CDS and `three_prime_utr` if UTR is located after CDS.

## Setup


```shell
pip install cython
pip install -e git+https://github.com/MuhammedHasan/gencode_utr_fix.git#egg=gencode_utr_fix
```


## Run

```shell
gencode_utr_fix --input_gtf gencode.v29.annotation.gtf --output_gtf gencode.v29.annotation_utr.gtf
```


## Test
```
pytest tests/
```

## Cite
This package is based on [pyranges](https://github.com/biocore-ntnu/pyranges) so cite the pyranges paper if you are using this package for research: 

pyranges: http://dx.doi.org/10.1093/bioinformatics/btz615
