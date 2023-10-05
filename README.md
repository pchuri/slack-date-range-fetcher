# Slack Date Range Fetcher

## Description

This Python script fetches messages from a specified Slack channel within a given date range. It also retrieves and displays user information related to each message.

## Requirements

- Python 3.x
- Slack API Token

## Installation

1. Set up and activate the virtual environment.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .\.venv\Scripts\activate  # Windows
    ```

2. Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root and set the Slack API Token.
    ```
    BOT_TOKEN=your_bot_token_here
    ```

## Usage

1. Run the script.
    ```bash
    python slack_date_range_fetcher.py [channel_id] [start_date] [end_date]
    ```
    - `channel_id`: ID of the Slack channel where the messages reside.
    - `start_date`: Start date to fetch messages (in YYYY-MM-DD format).
    - `end_date`: End date to fetch messages (in YYYY-MM-DD format).

## Example

```bash
python slack_date_range_fetcher.py C123ABC456 2022-01-01 2022-01-31
```