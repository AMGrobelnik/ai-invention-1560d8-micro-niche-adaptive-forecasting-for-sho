#!/usr/bin/env python3
"""Custom JSON schema validator with detailed error reporting."""

import json
from pathlib import Path
from jsonschema import validate, ValidationError, SchemaError
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    data_file = Path("full_data_out.json")
    schema_file = Path("exp_sel_data_out_schema.json")

    logger.info(f"Loading data from {data_file}")
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        logger.error(f"Data file not found: {data_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in data file: {data_file} - {e}")
        sys.exit(1)

    logger.info(f"Loading schema from {schema_file}")
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except FileNotFoundError:
        logger.error(f"Schema file not found: {schema_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in schema file: {schema_file} - {e}")
        sys.exit(1)

    logger.info("Starting validation...")
    try:
        validate(instance=data, schema=schema)
        logger.info("Validation PASSED")
        sys.exit(0)
    except ValidationError as e:
        logger.error("Validation FAILED")
        logger.error(f"Error: {e.message}")
        logger.error(f"Path: {' -> '.join([str(p) for p in e.absolute_path]) if e.absolute_path else 'root'}")
        logger.error(f"Validator: {e.validator}")
        logger.error(f"Value: {e.instance}") # Log the actual value that failed validation
        sys.exit(1)
    except SchemaError as e:
        logger.error("Schema validation error (the schema itself is invalid)")
        logger.error(f"Error: {e.message}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred during validation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
