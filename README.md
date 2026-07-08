# Automated Lab Data Processor

    Plate-reader QC and dose-response analysis for a synthetic 96-well assay.

    ## Dataset

    Synthetic dose-response plate data generated from public assay design conventions.

    ## Methods

    - Z-factor from controls
- Replicate CV by dose
- Dose-response ready tidy table
- Reusable Claude command prompts

    ## Reproduce

    ```bash
    python scripts/run_pipeline.py
    ```

    ## Outputs

    - `data/plate_reader.csv`
- `outputs/qc_summary.csv`
- `outputs/replicate_cv.csv`
- `figures/qc_summary.svg`

    ## Portfolio Note

    This repository uses public or synthetic demonstration data only. It is
    intended to show reproducible computational biology and AI/ML workflow
    design without relying on confidential or employer-owned material.
