# Automated Lab Data Processor

Plate-reader QC and dose-response analysis for a synthetic 96-well assay. This repo now includes the missing dose-response endpoint: a tidy dose summary and an estimated IC50 table for each compound, alongside Z-factor and replicate CV quality metrics.

## Reproduce

```bash
python scripts/run_pipeline.py
```

## Outputs

- `data/plate_reader.csv`
- `outputs/qc_summary.csv`
- `outputs/replicate_cv.csv`
- `outputs/dose_response_summary.csv`
- `outputs/ic50_summary.csv`
- `figures/qc_summary.svg`
- `figures/dose_response_ic50.svg`

## Analysis Report

Open `reports/analysis_report.html` for the hypothesis, public data provenance, process, outputs, and interpretation.

## Portfolio Note

This repository uses public data sources or clearly labelled synthetic demonstration data only. No employer-owned or confidential data are included.
