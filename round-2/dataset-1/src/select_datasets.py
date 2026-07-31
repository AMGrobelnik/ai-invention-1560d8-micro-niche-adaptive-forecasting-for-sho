#!/usr/bin/env python3
"""Selects the top 10 datasets from the full dataset and saves them to a new JSON file."""

import json
from pathlib import Path
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    input_path = Path("full_data_out.json")
    output_path = Path("selected_datasets.json")
    num_datasets_to_select = 10

    logger.info(f"Loading full dataset from {input_path}")
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    try:
        full_data = json.loads(input_path.read_text())
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in full data file: {input_path} - {e}")
        sys.exit(1)

    all_datasets = full_data.get("datasets", [])
    if not all_datasets:
        logger.error("No datasets found in the input file.")
        sys.exit(1)

    # Select the first N datasets. Since the generation script shuffled them, 
    # taking the first N provides a diverse sample.
    selected_datasets = all_datasets[:num_datasets_to_select]

    final_output = {"datasets": selected_datasets}

    output_path.write_text(json.dumps(final_output, indent=2))
    logger.info(f"Selected {len(selected_datasets)} datasets and saved to {output_path}.")

if __name__ == "__main__":
    main()
