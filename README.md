# Magnificent 7 Stocks - Moving Averages Tracker

Automated tracking of 8-day, 21-day, 50-day, and 200-day moving averages for the Magnificent 7 tech stocks.

## Stocks Tracked
- **AAPL** - Apple
- **MSFT** - Microsoft
- **GOOGL** - Google/Alphabet
- **AMZN** - Amazon
- **META** - Meta/Facebook
- **TSLA** - Tesla
- **NVDA** - Nvidia

## Features
- Automatically fetches latest stock data from Yahoo Finance
- Calculates multiple moving averages (8d, 21d, 50d, 200d)
- Shows percentage difference from current price
- Saves results to CSV for easy analysis
- Runs automatically every weekday after market close via GitHub Actions

## Local Usage

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/mag7-moving-averages.git
cd mag7-moving-averages

# Install dependencies
pip install -r requirements.txt

# Run the script
python mag7_moving_averages.py
```

## GitHub Actions Automation

This repository is configured to automatically update the moving averages data:

- **Schedule**: Runs every weekday at 5 PM EST (after US market close)
- **Manual Trigger**: You can also run it manually from the Actions tab
- **Auto-commit**: Results are automatically committed to `mag7_moving_averages.csv`

### Setup Instructions

1. **Fork or create this repository on GitHub**

2. **Enable GitHub Actions**:
   - Go to your repository on GitHub
   - Click on the "Actions" tab
   - Enable workflows if prompted

3. **Grant write permissions** (required for auto-commits):
   - Go to Settings → Actions → General
   - Scroll to "Workflow permissions"
   - Select "Read and write permissions"
   - Click Save

4. **Manual run** (optional):
   - Go to Actions tab
   - Click "Update Mag 7 Moving Averages"
   - Click "Run workflow"

## Output

The script generates:
1. **Console output**: Formatted table showing all data
2. **CSV file** (`mag7_moving_averages.csv`): Spreadsheet with all results

### CSV Columns
- Ticker
- Current Price
- Date
- 8d MA, 8d MA % (difference from current)
- 21d MA, 21d MA % (difference from current)
- 50d MA, 50d MA % (difference from current)
- 200d MA, 200d MA % (difference from current)

## Understanding the Data

### Moving Averages Explained
- **8-day MA**: Very short-term trend indicator
- **21-day MA**: Short-term trend (approximately 1 trading month)
- **50-day MA**: Medium-term trend indicator
- **200-day MA**: Long-term trend (the "golden" moving average)

### Percentage Difference
- **Positive %**: Stock is trading above the moving average (bullish signal)
- **Negative %**: Stock is trading below the moving average (bearish signal)

## Data Source
All data is fetched from Yahoo Finance via the `yfinance` Python library.

## License
MIT License - Feel free to use and modify as needed.

## Disclaimer
This tool is for informational purposes only. It does not constitute financial advice. Always do your own research before making investment decisions.
