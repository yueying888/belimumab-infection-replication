# Belimumab infection-safety cross-system replication

Publication-facing reproducibility materials for “Prespecified cross-system replication and robustness of infection safety evidence with belimumab in systemic lupus erythematosus: a FAERS–JADER disproportionality analysis”.

## Scope

This release regenerates publication tables and verifies figure-source completeness from aggregate CSV files. It does not redistribute FAERS or JADER bulk source data, licensed MedDRA terminology, or patient-level local clinical data. Upstream case selection therefore requires independent acquisition of source data and terminology rights.

## Reproduce

Use Python 3.14 or a compatible Python 3 version:

```bash
python scripts/reproduce_publication_outputs.py
```

The script writes CSV copies and a machine-readable validation report to `reproduced/`.

## Version and citation

This clean-history repository is prepared as version `v1.0.0`. Cite the associated article and use `CITATION.cff` for machine-readable author and title metadata. A repository URL or DOI will be added only after the release is publicly deposited; none is claimed in this pre-publication package.

## Release boundary

No causal, incidence, treatment-effect, or local event-rate claim is supported by this package. No license grant is included in this release; all rights remain with the authors.
