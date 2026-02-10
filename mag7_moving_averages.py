#!/usr/bin/env python3
"""
Script to calculate 8-day, 21-day, 50-day, and 200-day moving averages
for the Magnificent 7 stocks (AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA)

INSTALLATION:
    pip install yfinance pandas

USAGE:
    python mag7_moving_averages.py
    
OUTPUT:
    - Console output showing all moving averages
    - CSV file: mag7_moving_averages.csv
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Magnificent 7 stock tickers
MAG7_TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA']

# Moving average periods
MA_PERIODS = [8, 21, 50, 200]

def get_moving_averages(ticker, periods=[8, 21, 50, 200]):
    """
    Calculate moving averages for a given ticker
    
    Args:
        ticker: Stock ticker symbol
        periods: List of periods for moving averages
        
    Returns:
        Dictionary with current price and moving averages
    """
    try:
        # Download data - get extra days to ensure we have enough for 200-day MA
        stock = yf.Ticker(ticker)
        df = stock.history(period='1y')
        
        if df.empty:
            return None
        
        # Calculate moving averages
        result = {
            'Ticker': ticker,
            'Current Price': round(df['Close'].iloc[-1], 2),
            'Date': df.index[-1].strftime('%Y-%m-%d')
        }
        
        for period in periods:
            ma_value = df['Close'].rolling(window=period).mean().iloc[-1]
            result[f'{period}d MA'] = round(ma_value, 2)
            
            # Calculate percentage difference from current price
            pct_diff = ((result['Current Price'] - ma_value) / ma_value) * 100
            result[f'{period}d MA %'] = round(pct_diff, 2)
        
        return result
        
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None

def main():
    """Main function to calculate and display moving averages for all Mag 7 stocks"""
    
    print("=" * 100)
    print("MAGNIFICENT 7 STOCKS - MOVING AVERAGES")
    print("=" * 100)
    print(f"Data as of: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)
    print()
    
    all_results = []
    
    for ticker in MAG7_TICKERS:
        print(f"Fetching data for {ticker}...")
        result = get_moving_averages(ticker, MA_PERIODS)
        
        if result:
            all_results.append(result)
    
    # Create DataFrame for better display
    df_results = pd.DataFrame(all_results)
    
    # Reorder columns for better readability
    columns_order = ['Ticker', 'Current Price', 'Date']
    for period in MA_PERIODS:
        columns_order.extend([f'{period}d MA', f'{period}d MA %'])
    
    df_results = df_results[columns_order]
    
    print("\n" + "=" * 100)
    print("RESULTS:")
    print("=" * 100)
    print()
    
    # Display each stock's data
    for _, row in df_results.iterrows():
        print(f"\n{row['Ticker']} - Current Price: ${row['Current Price']:.2f} (as of {row['Date']})")
        print("-" * 80)
        for period in MA_PERIODS:
            ma_col = f'{period}d MA'
            pct_col = f'{period}d MA %'
            print(f"  {period:3d}-day MA: ${row[ma_col]:8.2f}  ({row[pct_col]:+6.2f}% from current)")
    
    print("\n" + "=" * 100)
    print("\nSummary Table:")
    print("=" * 100)
    
    # Create a simplified summary table
    summary_df = df_results[['Ticker', 'Current Price'] + [f'{p}d MA' for p in MA_PERIODS]].copy()
    print(summary_df.to_string(index=False))
    
    # Optional: Save to CSV
    output_file = 'mag7_moving_averages.csv'
    df_results.to_csv(output_file, index=False)
    print(f"\n\nData saved to: {output_file}")
    print("=" * 100)

if __name__ == "__main__":
    main()
