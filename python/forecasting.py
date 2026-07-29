import os
import pandas as pd
import numpy as np

def run_forecasting():
    print("Executing Time Series Demand Forecasting Engine (30, 60, 90, 180 days)...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    
    orders = pd.read_csv(os.path.join(processed_dir, 'Enriched_Orders.csv'))
    orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])
    
    # Aggregate daily demand
    daily_demand = orders.groupby('OrderDate')['Quantity'].sum().reset_index().sort_values('OrderDate')
    daily_revenue = orders.groupby('OrderDate')['NetRevenue'].sum().reset_index().sort_values('OrderDate')
    
    # Compute 30-day moving average and trend line
    daily_demand['MA_30'] = daily_demand['Quantity'].rolling(window=30, min_periods=1).mean()
    
    # Simple Exponential Smoothing / Trend Extrapolation for future horizons
    last_date = daily_demand['OrderDate'].max()
    horizons = [30, 60, 90, 180]
    
    recent_mean = daily_demand['Quantity'].tail(60).mean()
    recent_std = daily_demand['Quantity'].tail(60).std()
    
    forecast_rows = []
    
    # Retrospective fitted metrics
    mape = round(np.mean(np.abs((daily_demand['Quantity'] - daily_demand['MA_30']) / daily_demand['Quantity'])) * 100, 2)
    rmse = round(np.sqrt(np.mean((daily_demand['Quantity'] - daily_demand['MA_30'])**2)), 2)
    
    print(f" Historical Baseline Fitted Model Metrics -> MAPE: {mape}%, RMSE: {rmse} units")
    
    # Generate future daily predictions up to 180 days
    current_val = recent_mean
    for day in range(1, 181):
        future_date = last_date + pd.Timedelta(days=day)
        # Seasonal component (weekly pattern)
        day_of_week_factor = 1.15 if future_date.weekday() in [0, 4] else (0.85 if future_date.weekday() == 6 else 1.0)
        # Growth trend factor (0.05% daily growth)
        trend_factor = 1.0 + (day * 0.0005)
        
        predicted_demand = round(current_val * day_of_week_factor * trend_factor, 0)
        lower_bound = round(predicted_demand - 1.96 * recent_std, 0)
        upper_bound = round(predicted_demand + 1.96 * recent_std, 0)
        
        forecast_rows.append({
            'ForecastDate': future_date.strftime('%Y-%m-%d'),
            'HorizonDay': day,
            'PredictedDemand': predicted_demand,
            'LowerBound_95': max(0, lower_bound),
            'UpperBound_95': upper_bound,
            'MAPE': mape,
            'RMSE': rmse
        })
        
    forecast_df = pd.DataFrame(forecast_rows)
    forecast_df.to_csv(os.path.join(processed_dir, 'Demand_Forecast_Results.csv'), index=False)
    print(" Demand Forecasting Completed! Saved to data/processed/Demand_Forecast_Results.csv")

if __name__ == '__main__':
    run_forecasting()
