# README - Vivado Automation & Data Processing

## Overview
This project automates Vivado execution and extracts key metrics (power, delay, LUTs) from report files.

## Workflow
1. **Vivado Automation**
   - Lists modules in `Modules/`.
   - Runs Vivado batch mode (`tcl_create.tcl`, `tcl_add.tcl`, `tcl_run.tcl`).
   - Saves results in `results/`.

2. **Data Processing**
   - Reads `power.txt`, `timing.txt`, `utilization.txt`.
   - Extracts `Total On-Chip Power`, `Data Path Delay`, `Slice LUTs`.
   - Saves results in `Final_results.csv`.

## Requirements
- Python 3.x, Vivado (CLI access), `numpy`, `pandas`.

## Usage
```bash
python vivado_automation.py
python process_results.py
```

## Notes
- Ensure Vivado is in system path.
- Modify TCL scripts as needed.

## License
Open-source, free for academic and research use.

