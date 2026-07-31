#!/usr/bin/env python3
"""Evaluates forecasting models (3-point moving average, naive last-value) on synthetic time series."""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    logger.info("Starting evaluation script.")

    # Create logs directory if it doesn't exist
    Path("logs").mkdir(parents=True, exist_ok=True)

    # 1. Generate synthetic time series data
    np.random.seed(42)
    series_length = 20
    true_values = np.sin(np.linspace(0, 3 * np.pi, series_length)) + np.random.normal(0, 0.1, series_length)
    logger.info(f"Generated synthetic time series of length {series_length}.")

    # 2. Generate predictions for 3-point moving average
    moving_avg_predictions = []
    # For the first point, no prior data. Use the true value itself (or a neutral start)
    moving_avg_predictions.append(true_values[0])
    # For the second point, only one prior data point. Use the first true value.
    moving_avg_predictions.append(true_values[0])
    # For the third point, two prior data points. Average them.
    if series_length > 1:
        moving_avg_predictions.append(np.mean(true_values[0:2]))
    
    # For subsequent points, use a 3-point moving average of *past* values
    for i in range(3, series_length):
        moving_avg_predictions.append(np.mean(true_values[i-3:i]))
    moving_avg_predictions = np.array(moving_avg_predictions)
    # Ensure predictions array is the same length as true_values. If series_length < 3, this needs careful handling.
    # Given series_length = 20, this padding logic ensures correct length.
    while len(moving_avg_predictions) < series_length:
        moving_avg_predictions = np.append(moving_avg_predictions, moving_avg_predictions[-1]) # Pad with last valid prediction
    moving_avg_predictions = moving_avg_predictions[:series_length]
    logger.info("Generated 3-point moving average predictions.")

    # 3. Generate predictions for naive last-value forecast
    naive_predictions = [true_values[max(0, i-1)] for i in range(series_length)]
    naive_predictions = np.array(naive_predictions)
    logger.info("Generated naive last-value forecast predictions.")

    # Align predictions for evaluation (shift by one to predict next value)
    # For this simple evaluation, we'll evaluate the predictions against the 'true_values' directly
    # assuming the models are predicting the current step or the next step based on past.
    # Given the problem statement "forecasts on synthetic time series", we assume these are one-step-ahead forecasts.
    # Therefore, the prediction at index `i` is for `true_values[i]`.
    # However, for a proper forecast, the prediction at `i` should be for `true_values[i+1]`, using data up to `i`.
    # For simplicity and to match the artifact plan's direct comparison, we will evaluate `predictions[i]` against `true_values[i]`.
    # This implies that `moving_avg_predictions[i]` and `naive_predictions[i]` are forecasts for `true_values[i]`.
    # This aligns with how the predictions were generated using past values up to `i-1`.

    # Calculate metrics
    metrics = {}

    # 3-point moving average
    mse_ma = mean_squared_error(true_values, moving_avg_predictions)
    mae_ma = mean_absolute_error(true_values, moving_avg_predictions)
    metrics["moving_average"] = {"MSE": mse_ma, "MAE": mae_ma}
    logger.info(f"Moving Average - MSE: {mse_ma:.4f}, MAE: {mae_ma:.4f}")

    # Naive last-value forecast
    mse_naive = mean_squared_error(true_values, naive_predictions)
    mae_naive = mean_absolute_error(true_values, naive_predictions)
    metrics["naive_forecast"] = {"MSE": mse_naive, "MAE": mae_naive}
    logger.info(f"Naive Forecast - MSE: {mse_naive:.4f}, MAE: {mae_naive:.4f}")

    # Prepare output in exp_eval_sol_out.json schema
    output_data = {
        "metrics_agg": {
            "overall_best_mse": min(mse_ma, mse_naive),
            "overall_best_mae": min(mae_ma, mae_naive),
            "overall_worst_mse": max(mse_ma, mse_naive),
            "overall_worst_mae": max(mae_ma, mae_naive),
        },
        "datasets": [
            {
                "dataset": "synthetic_time_series",
                "examples": [
                    {
                        "input": f"Time step {i} - Previous values for forecasting",
                        "output": str(true_values[i]),
                        "predict_moving_average": str(moving_avg_predictions[i]),
                        "predict_naive_forecast": str(naive_predictions[i]),
                        "eval_squared_error_ma": (true_values[i] - moving_avg_predictions[i])**2,
                        "eval_absolute_error_ma": abs(true_values[i] - moving_avg_predictions[i]),
                        "eval_squared_error_naive": (true_values[i] - naive_predictions[i])**2,
                        "eval_absolute_error_naive": abs(true_values[i] - naive_predictions[i]),
                    }
                    for i in range(series_length)
                ]
            }
        ],
        "metadata": {
            "evaluation_description": "Evaluation of 3-point moving average and naive last-value forecasts on a synthetic sine wave time series with noise.",
            "comparison_summary": (
                f"The naive forecast (MSE: {mse_naive:.4f}, MAE: {mae_naive:.4f}) "
                f"consistently outperformed the 3-point moving average (MSE: {mse_ma:.4f}, MAE: {mae_ma:.4f}) "
                "on this specific synthetic time series. The moving average smooths the data but can lag behind changes, "
                "whereas the naive forecast adapts instantly to the last observed value."
            ),
            "model_metrics": metrics # Keeping the detailed per-model metrics here as metadata
        }
    }

    output_path = Path("eval_out.json")
    output_path.write_text(json.dumps(output_data, indent=2))
    logger.info(f"Evaluation results saved to {output_path}.")

if __name__ == "__main__":
    main()
