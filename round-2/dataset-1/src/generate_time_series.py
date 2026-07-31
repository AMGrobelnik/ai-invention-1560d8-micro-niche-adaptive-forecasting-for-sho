#!/usr/bin/env python3
"""Generates diverse synthetic time series datasets."""

import json
import random
import math
from pathlib import Path
from loguru import logger
import sys
import numpy as np

# --- Logging Setup ---
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# --- Hardware Detection (Simplified for this task, as we're not using advanced hardware features directly) ---
# For a pure CPU-bound task, we primarily care about NUM_CPUS for multiprocessing.
# For memory, we'll monitor and if needed, add explicit resource limits.

# Placeholder for NUM_CPUS - in a real scenario, use _detect_cpus() from aii-use-hardware
NUM_CPUS = 1 # Default, will be updated if we use multiprocessing.

@logger.catch(reraise=True)
def generate_linear_trend_series(series_id, length, noise_level, trend_type):
    """Generates a time series with a linear trend."""
    data = []
    start_value = random.uniform(50, 150)
    if trend_type == "upward":
        slope = random.uniform(0.5, 2.0)
    else:  # "downward"
        slope = random.uniform(-2.0, -0.5)

    for i in range(length):
        value = start_value + slope * i + random.gauss(0, noise_level)
        data.append(value)
    return {
        "series_id": series_id,
        "data": data,
        "metadata": {
            "pattern_type": "linear_trend",
            "trend_type": trend_type,
            "slope": slope,
            "noise_level": noise_level,
            "length": length,
        },
    }

@logger.catch(reraise=True)
def generate_flat_series(series_id, length, noise_level):
    """Generates a relatively constant time series."""
    data = []
    constant_value = random.uniform(80, 120)
    for _ in range(length):
        value = constant_value + random.gauss(0, noise_level)
        data.append(value)
    return {
        "series_id": series_id,
        "data": data,
        "metadata": {
            "pattern_type": "flat",
            "constant_value": constant_value,
            "noise_level": noise_level,
            "length": length,
        },
    }

@logger.catch(reraise=True)
def generate_oscillatory_series(series_id, length, noise_level, frequency_range, amplitude_range):
    """Generates a time series with an oscillatory (sine) pattern."""
    data = []
    amplitude = random.uniform(*amplitude_range)
    frequency = random.uniform(*frequency_range)
    phase = random.uniform(0, 2 * math.pi)
    offset = random.uniform(80, 120)

    for i in range(length):
        value = offset + amplitude * math.sin(2 * math.pi * frequency * i + phase) + random.gauss(0, noise_level)
        data.append(value)
    return {
        "series_id": series_id,
        "data": data,
        "metadata": {
            "pattern_type": "oscillatory",
            "amplitude": amplitude,
            "frequency": frequency,
            "noise_level": noise_level,
            "length": length,
        },
    }

@logger.catch(reraise=True)
def generate_step_change_series(series_id, length, noise_level):
    """Generates a time series with a sudden step change."""
    data = []
    base_value = random.uniform(50, 100)
    step_change_magnitude = random.uniform(20, 50) * random.choice([-1, 1])
    step_point = random.randint(3, length - 3)

    for i in range(length):
        value = base_value
        if i >= step_point:
            value += step_change_magnitude
        value += random.gauss(0, noise_level)
        data.append(value)
    return {
        "series_id": series_id,
        "data": data,
        "metadata": {
            "pattern_type": "step_change",
            "base_value": base_value,
            "step_change_magnitude": step_change_magnitude,
            "step_point": step_point,
            "noise_level": noise_level,
            "length": length,
        },
    }

@logger.catch(reraise=True)
def generate_volatility_shift_series(series_id, length, base_noise_level):
    """Generates a time series where noise/volatility shifts."""
    data = []
    start_value = random.uniform(80, 120)
    shift_point = random.randint(3, length - 3)
    volatility_multiplier = random.uniform(2, 5)

    for i in range(length):
        current_noise_level = base_noise_level
        if i >= shift_point:
            current_noise_level *= volatility_multiplier
        value = start_value + random.gauss(0, current_noise_level)
        data.append(value)
    return {
        "series_id": series_id,
        "data": data,
        "metadata": {
            "pattern_type": "volatility_shift",
            "start_value": start_value,
            "base_noise_level": base_noise_level,
            "volatility_multiplier": volatility_multiplier,
            "shift_point": shift_point,
            "length": length,
        },
    }

@logger.catch(reraise=True)
def generate_combined_series(series_id, length, noise_level):
    """Generates a time series combining two patterns."""
    data = []
    pattern_choices = ["linear_trend", "oscillatory", "flat", "step_change"]
    # Ensure two distinct patterns for combination
    pattern1_type = random.choice(pattern_choices)
    pattern2_type = random.choice([p for p in pattern_choices if p != pattern1_type])

    mid_point = random.randint(length // 3, 2 * length // 3)

    # Generate first part
    part1_length = mid_point
    part1_series = []
    if pattern1_type == "linear_trend":
        part1_series = generate_linear_trend_series(f"{series_id}_p1", part1_length, noise_level, random.choice(["upward", "downward"]))["data"]
    elif pattern1_type == "oscillatory":
        part1_series = generate_oscillatory_series(f"{series_id}_p1", part1_length, noise_level, (0.05, 0.2), (5, 15))["data"]
    elif pattern1_type == "flat":
        part1_series = generate_flat_series(f"{series_id}_p1", part1_length, noise_level)["data"]
    elif pattern1_type == "step_change":
        part1_series = generate_step_change_series(f"{series_id}_p1", part1_length, noise_level)["data"]

    # Generate second part, trying to make it somewhat continuous if possible
    part2_length = length - mid_point
    part2_series = []
    if part2_length > 0: # Ensure part2 has a valid length
        # Adjust start of second series to be closer to end of first
        start_value_for_part2 = part1_series[-1] if part1_series else random.uniform(50,150)
        
        if pattern2_type == "linear_trend":
            temp_series = generate_linear_trend_series(f"{series_id}_p2", part2_length, noise_level, random.choice(["upward", "downward"]))
            # Adjust to be continuous
            adjustment = start_value_for_part2 - temp_series["data"][0]
            part2_series = [val + adjustment for val in temp_series["data"]]
        elif pattern2_type == "oscillatory":
            temp_series = generate_oscillatory_series(f"{series_id}_p2", part2_length, noise_level, (0.05, 0.2), (5, 15))
            adjustment = start_value_for_part2 - temp_series["data"][0]
            part2_series = [val + adjustment for val in temp_series["data"]]
        elif pattern2_type == "flat":
            temp_series = generate_flat_series(f"{series_id}_p2", part2_length, noise_level)
            adjustment = start_value_for_part2 - temp_series["data"][0]
            part2_series = [val + adjustment for val in temp_series["data"]]
        elif pattern2_type == "step_change":
            temp_series = generate_step_change_series(f"{series_id}_p2", part2_length, noise_level)
            adjustment = start_value_for_part2 - temp_series["data"][0]
            part2_series = [val + adjustment for val in temp_series["data"]]

    data = part1_series + part2_series

    return {
        "series_id": series_id,
        "data": data,
        "metadata": {
            "pattern_type": "combined",
            "pattern1_type": pattern1_type,
            "pattern2_type": pattern2_type,
            "mid_point": mid_point,
            "noise_level": noise_level,
            "length": length,
        },
    }


def main():
    output_dir = Path("generated_datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    all_series_data = []
    target_num_datasets = 50 # As per artifact plan
    series_length_range = (10, 20)
    noise_level = 1.0 # Base noise level

    # Set a fixed random seed for reproducibility
    random.seed(42)
    np.random.seed(42)

    generation_functions = [
        ("linear_trend_up", lambda sid, length: generate_linear_trend_series(sid, length, noise_level, "upward")),
        ("linear_trend_down", lambda sid, length: generate_linear_trend_series(sid, length, noise_level, "downward")),
        ("flat", lambda sid, length: generate_flat_series(sid, length, noise_level)),
        ("oscillatory", lambda sid, length: generate_oscillatory_series(sid, length, noise_level, (0.05, 0.2), (5, 15))),
        ("step_change", lambda sid, length: generate_step_change_series(sid, length, noise_level)),
        ("volatility_shift", lambda sid, length: generate_volatility_shift_series(sid, length, noise_level)),
        ("combined", lambda sid, length: generate_combined_series(sid, length, noise_level)),
    ]

    # Distribute generation across patterns
    series_per_pattern = target_num_datasets // len(generation_functions)
    remaining_series = target_num_datasets % len(generation_functions)

    series_id_counter = 0
    for pattern_name, generate_func in generation_functions:
        num_to_generate = series_per_pattern
        if remaining_series > 0:
            num_to_generate += 1
            remaining_series -= 1

        for _ in range(num_to_generate):
            series_id_counter += 1
            length = random.randint(*series_length_range)
            series = generate_func(f"series_{series_id_counter:03d}", length)
            all_series_data.append(series)

    # Ensure exactly target_num_datasets are generated, if there's a slight off-by-one from division
    while len(all_series_data) < target_num_datasets:
        series_id_counter += 1
        length = random.randint(*series_length_range)
        pattern_name, generate_func = random.choice(generation_functions)
        series = generate_func(f"series_{series_id_counter:03d}", length)
        all_series_data.append(series)
    
    # Shuffle to mix up pattern types
    random.shuffle(all_series_data)


    # Save the full dataset
    full_output_path = output_dir / "full_synthetic_time_series_dataset.json"
    full_output_content = json.dumps(all_series_data, indent=2)
    full_output_path.write_text(full_output_content)
    logger.info(f"Generated and saved full dataset to {full_output_path}")

    # Generate mini and preview versions using the aii-json skill's script
    # This requires invoking a separate script, which will be done in the next step.

if __name__ == "__main__":
    main()
