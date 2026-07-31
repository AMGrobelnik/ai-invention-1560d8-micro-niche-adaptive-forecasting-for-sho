import json
import math

def calculate_mse(actual, predictions):
    if not actual or not predictions or len(actual) != len(predictions):
        return None
    sum_sq_error = sum([(a - p) ** 2 for a, p in zip(actual, predictions)])
    return sum_sq_error / len(actual)

def calculate_mae(actual, predictions):
    if not actual or not predictions or len(actual) != len(predictions):
        return None
    sum_abs_error = sum([abs(a - p) for a, p in zip(actual, predictions)])
    return sum_abs_error / len(actual)

def naive_forecast(series, forecast_horizon):
    if not series:
        return []
    last_value = series[-1]
    return [last_value] * forecast_horizon

def moving_average_forecast(series, window_size, forecast_horizon):
    if len(series) < window_size:
        return [series[-1]] * forecast_horizon if series else [] # Fallback to naive if not enough data for MA
    
    # Calculate initial moving average based on the last 'window_size' points
    ma_value = sum(series[-window_size:]) / window_size
    return [ma_value] * forecast_horizon

def evaluate_forecasts(synthetic_series_path, method_out_path):
    with open(synthetic_series_path, 'r') as f:
        synthetic_series_data = json.load(f)
    
    with open(method_out_path, 'r') as f:
        method_out_data = json.load(f)

    all_results = []
    
    overall_mse_naive = 0
    overall_mae_naive = 0
    overall_mse_ma = 0
    overall_mae_ma = 0
    overall_mse_adaptive = 0
    overall_mae_adaptive = 0
    
    total_forecasts = 0

    for i, series in enumerate(synthetic_series_data):
        # Find corresponding results from method_out_data
        method_series_result = None
        for example in method_out_data['datasets'][0]['examples']:
            if example['metadata_series_id'] == i:
                method_series_result = example
                break
        
        if not method_series_result:
            print(f"Warning: No method_out_data found for series_id {i}")
            continue

        actual_values = json.loads(method_series_result['output'])
        
        # Ensure that actual_values exist and are not empty before proceeding
        if not actual_values:
            print(f"Warning: No actual_values found for series_id {i}")
            continue

        forecast_horizon = len(actual_values)
        
        # Generate naive forecasts
        predictions_naive = naive_forecast(series[:-forecast_horizon], forecast_horizon)

        # Generate 3-point moving average forecasts
        window_size = 3
        predictions_ma = moving_average_forecast(series[:-forecast_horizon], window_size, forecast_horizon)

        # Get adaptive forecasts from method_out_data
        predictions_adaptive = json.loads(method_series_result['predict_adaptive'])
        
        # Calculate metrics
        mse_naive = calculate_mse(actual_values, predictions_naive)
        mae_naive = calculate_mae(actual_values, predictions_naive)
        
        mse_ma = calculate_mse(actual_values, predictions_ma)
        mae_ma = calculate_mae(actual_values, predictions_ma)
        
        mse_adaptive = calculate_mse(actual_values, predictions_adaptive)
        mae_adaptive = calculate_mae(actual_values, predictions_adaptive)

        all_results.append({
            "metadata_series_id": i, # Rename series_id to metadata_series_id
            "input": json.dumps(series), # Add original series as input, convert to string
            "output": json.dumps(actual_values), # Rename actual_values to output, convert to string
            "predict_naive": json.dumps(predictions_naive),
            "predict_ma": json.dumps(predictions_ma),
            "predict_adaptive": json.dumps(predictions_adaptive),
            "eval_mse_naive": mse_naive,
            "eval_mae_naive": mae_naive,
            "eval_mse_ma": mse_ma,
            "eval_mae_ma": mae_ma,
            "eval_mse_adaptive": mse_adaptive,
            "eval_mae_adaptive": mae_adaptive
        })
        
        overall_mse_naive += mse_naive
        overall_mae_naive += mae_naive
        overall_mse_ma += mse_ma
        overall_mae_ma += mae_ma
        overall_mse_adaptive += mse_adaptive
        overall_mae_adaptive += mae_adaptive
        total_forecasts += 1
    
    final_output = {
        "datasets": [
            {
                "dataset": "Synthetic Time Series Forecast Evaluation",
                "examples": all_results
            }
        ],
        "metrics_agg": {
            "avg_mse_naive": overall_mse_naive / total_forecasts,
            "avg_mae_naive": overall_mae_naive / total_forecasts,
            "avg_mse_ma": overall_mse_ma / total_forecasts,
            "avg_mae_ma": overall_mae_ma / total_forecasts,
            "avg_mse_adaptive": overall_mse_adaptive / total_forecasts,
            "avg_mae_adaptive": overall_mae_adaptive / total_forecasts
        }
    }
    
    return final_output

if __name__ == '__main__':
    synthetic_series_path = "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/synthetic_time_series.json"
    method_out_path = "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method_out.json"
    
    evaluation_results = evaluate_forecasts(synthetic_series_path, method_out_path)
    
    output_file_path = "/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/eval_out.json"
    with open(output_file_path, 'w') as f:
        json.dump(evaluation_results, f, indent=4)
    print(f"Evaluation results saved to {output_file_path}")
