#!/usr/bin/env python3
"""Loads generated synthetic time series and standardizes to exp_sel_data_out.json schema."""

import json
from pathlib import Path
from loguru import logger
import sys

# --- Logging Setup ---
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    raw_series_input_path = Path("temp/datasets/full_synthetic_time_series_dataset.json")
    selected_datasets_path = Path("selected_datasets.json")
    output_path = Path("full_data_out.json")

    logger.info(f"Loading raw series data from {raw_series_input_path}")
    if not raw_series_input_path.exists():
        logger.error(f"Input file not found: {raw_series_input_path}")
        sys.exit(1)

    all_raw_series = json.loads(raw_series_input_path.read_text())
    logger.info(f"Loaded {len(all_raw_series)} raw time series.")

    logger.info(f"Loading selected datasets from {selected_datasets_path}")
    if not selected_datasets_path.exists():
        logger.error(f"Selected datasets file not found: {selected_datasets_path}")
        sys.exit(1)

    selected_data = json.loads(selected_datasets_path.read_text())
    selected_series_ids = {ds["dataset"].replace("synthetic_series_", "") for ds in selected_data.get("datasets", [])}
    logger.info(f"Selected {len(selected_series_ids)} series IDs: {selected_series_ids}")

    filtered_raw_series = [s for s in all_raw_series if s["series_id"] in selected_series_ids]
    logger.info(f"Filtered raw series down to {len(filtered_raw_series)} series based on selection.")

    standardized_datasets = []

    for series_entry in filtered_raw_series:
        series_id = series_entry["series_id"]
        series_data = series_entry["data"]
        metadata = series_entry["metadata"]
        dataset_name = f"synthetic_series_{series_id}"

        examples = []
        # For time series forecasting, each example will be a window of data for prediction.
        # Let's use a fixed window size for input and predict the next value.
        # The problem implies a 3-point moving average, so an input window of at least 3 is logical.
        # We need at least 4 points to make a 3-point moving average prediction (3 input + 1 target).
        min_input_window_size = 3
        
        # Iterate to create multiple examples from each series
        for i in range(min_input_window_size, len(series_data)):
            input_sequence = series_data[i - min_input_window_size : i]
            output_value = series_data[i]

            example = {
                "input": json.dumps(input_sequence), # Input is a list of floats, convert to JSON string
                "output": str(output_value),        # Output is a single float, convert to string
                "metadata_series_id": series_id,
                "metadata_pattern_type": metadata["pattern_type"],
                "metadata_forecasting_point_index": i,
                "metadata_input_window_size": min_input_window_size,
            }
            examples.append(example)

        if examples:
            standardized_datasets.append({
                "dataset": dataset_name,
                "examples": examples
            })

    final_output = {"datasets": standardized_datasets}

    output_path.write_text(json.dumps(final_output, indent=2))
    logger.info(f"Standardized data saved to {output_path} with {len(standardized_datasets)} datasets and a total of {sum(len(d["examples"]) for d in standardized_datasets)} examples.")

if __name__ == "__main__":
    main()
