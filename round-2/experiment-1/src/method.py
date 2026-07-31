import json
import math

# Define Forecasting Models
def naive_forecast(series):
    if len(series) == 0:
        return None
    return series[-1]

def moving_average_forecast(series):
    if len(series) < 3:
        return naive_forecast(series) # Fallback for insufficient data
    return sum(series[-3:]) / 3

# Define Micro-Environmental Cues & Adaptive Logic
def calculate_local_cues(series):
    if len(series) < 3:
        return {'local_trend': 0, 'recent_volatility': 0} # Handle short series
    
    local_trend = series[-1] - series[-2]
    
    # Calculate standard deviation for volatility
    last_three_points = series[-3:]
    mean_last_three = sum(last_three_points) / 3
    recent_volatility = math.sqrt(sum((x - mean_last_three)**2 for x in last_three_points) / 3)
    
    return {'local_trend': local_trend, 'recent_volatility': recent_volatility}

def adaptive_forecast(series):
    if len(series) < 2: # Need at least two points for local_trend
        return naive_forecast(series) 
    if len(series) < 3: # Need at least three points for volatility, fallback to naive if not enough
        return naive_forecast(series)

    cues = calculate_local_cues(series)
    local_trend = cues['local_trend']
    recent_volatility = cues['recent_volatility']

    # Dynamic thresholds based on series magnitude
    # Use the mean of the last 3 points as a reference for magnitude
    if len(series) < 3:
        avg_magnitude = 1.0 # Default or handle as error
    else:
        avg_magnitude = sum(series[-3:]) / 3
    
    # If avg_magnitude is zero, avoid division by zero for relative thresholds
    if avg_magnitude == 0:
        # Fallback to absolute thresholds or default behavior if series is all zeros
        dynamic_trend_threshold = 1.0
        dynamic_volatility_threshold_for_trend = 0.5
        dynamic_volatility_threshold_for_MA = 1.5
    else:
        dynamic_trend_threshold = 0.1 * avg_magnitude
        dynamic_volatility_threshold_for_trend = 0.2 * avg_magnitude
        dynamic_volatility_threshold_for_MA = 0.3 * avg_magnitude

    if abs(local_trend) > dynamic_trend_threshold and recent_volatility < dynamic_volatility_threshold_for_trend:
        return naive_forecast(series) # Trending and stable
    elif recent_volatility > dynamic_volatility_threshold_for_MA:
        return moving_average_forecast(series) # Volatile or oscillating
    else:
        # Default or more nuanced decision; for simplicity, default to Naive
        return naive_forecast(series)

# Metrics Calculation
def calculate_mse(actual, predicted):
    # Filter out None values in predictions for cases where min_len is not met initially
    valid_pairs = [(a, p) for a, p in zip(actual, predicted) if p is not None]
    if not valid_pairs:
        return float('inf') # Or handle as appropriate
    return sum([(a - p)**2 for a, p in valid_pairs]) / len(valid_pairs)

def main():
    # Load Data
    data_filepath = '/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/synthetic_time_series.json'
    try:
        with open(data_filepath, 'r') as f:
            all_series = json.load(f)
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_filepath}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {data_filepath}")
        return


    results = []
    for i, series_data in enumerate(all_series):
        predictions_naive = []
        predictions_ma = []
        predictions_adaptive = []
        actual_values = []

        min_len_for_forecast = 3 # For 3P-MA and adaptive cues

        if len(series_data) < min_len_for_forecast + 1: # Need data for input AND next actual value
            # print(f"Skipping series {i} due to insufficient length: {len(series_data)} points.")
            continue # Skip very short series

        for t in range(min_len_for_forecast - 1, len(series_data) - 1): # Iterate up to second to last point
            current_series_window = series_data[:t+1] # Data available up to time t
            next_actual_value = series_data[t+1]

            # Make predictions
            predictions_naive.append(naive_forecast(current_series_window))
            predictions_ma.append(moving_average_forecast(current_series_window))
            predictions_adaptive.append(adaptive_forecast(current_series_window))
            actual_values.append(next_actual_value)

        # Calculate metrics for the current series
        mse_naive = calculate_mse(actual_values, predictions_naive)
        mse_ma = calculate_mse(actual_values, predictions_ma)
        mse_adaptive = calculate_mse(actual_values, predictions_adaptive)
        
        results.append({
            'series_id': i,
            'series_data': series_data, # Include for analysis
            'naive_mse': mse_naive,
            'ma_mse': mse_ma,
            'adaptive_mse': mse_adaptive,
            'predictions_naive': predictions_naive,
            'predictions_ma': predictions_ma,
            'predictions_adaptive': predictions_adaptive,
            'actual_values': actual_values
        })

    # Aggregate overall results
    if not results:
        overall_metrics = {'avg_mse_naive': float('inf'), 'avg_mse_ma': float('inf'), 'avg_mse_adaptive': float('inf')}
    else:
        overall_metrics = {
            'avg_mse_naive': sum(r['naive_mse'] for r in results if r['naive_mse'] != float('inf')) / len(results),
            'avg_mse_ma': sum(r['ma_mse'] for r in results if r['ma_mse'] != float('inf')) / len(results),
            'avg_mse_adaptive': sum(r['adaptive_mse'] for r in results if r['adaptive_mse'] != float('inf')) / len(results)
        }
    
    final_output = {
        "datasets": [
            {
                "dataset": "Synthetic Time Series",
                "examples": []
            }
        ],
        "metadata": {
            "overall_metrics": overall_metrics
        }
    }

    for r in results:
        example = {
            "input": json.dumps(r['series_data']),
            "output": json.dumps(r['actual_values']),
            "predict_naive": json.dumps(r['predictions_naive']),
            "predict_ma": json.dumps(r['predictions_ma']),
            "predict_adaptive": json.dumps(r['predictions_adaptive']),            "metadata_series_id": r['series_id'],
            "metadata_naive_mse": r['naive_mse'],
            "metadata_ma_mse": r['ma_mse'],
            "metadata_adaptive_mse": r['adaptive_mse']
        }
        final_output["datasets"][0]["examples"].append(example)

    # Save to method_out.json
    output_filepath = '/ai-inventor/aii_data/runs/run_x0ETRmd6GgXY/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method_out.json'
    with open(output_filepath, 'w') as f:
        json.dump(final_output, f, indent=4)
    print(f"Experiment results saved to {output_filepath}")

if __name__ == "__main__":
    main()
