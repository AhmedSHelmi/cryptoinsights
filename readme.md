```markdown
# CryptoInsights

CryptoInsights is a Flask-based web application that fetches historical cryptocurrency data, processes it, and sends the data to GPT-3 for investment recommendations. The application is containerized using Docker and includes an Nginx reverse proxy.

## Features

- Fetch historical cryptocurrency data from Binance.
- Calculate moving averages and filter data by date.
- Send processed data to GPT-3 for investment recommendations.
- Dockerized for easy deployment.
- Nginx reverse proxy for improved performance and security.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Binance API key and secret.
- OpenAI API key.

## Project Structure

```plaintext
/your_project
    /app
        __init__.py
        api.py
        binance_client.py
        data_processor.py
        gpt_service.py
        main.py
    Dockerfile
    requirements.txt
    docker-compose.yml
    nginx.conf
    run.py
```

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/AhmedSHelmi/cryptoinsights.git
cd cryptoinsights
```

2. **Add your API keys:**

Edit `app/api.py` to include your Binance and OpenAI API keys:

```python
BINANCE_API_KEY = 'YOUR_BINANCE_API_KEY'
BINANCE_API_SECRET = 'YOUR_BINANCE_API_SECRET'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
```

3. **Build and run the application using Docker Compose:**

```bash
docker-compose up --build -d
```

4. **Verify the setup:**

Open your web browser and navigate to `http://localhost/` to ensure the application is running correctly.

## Endpoints

- **POST /api/recommendations**: Get investment recommendations based on historical data.

### Request Body:

```json
{
    "symbol": "SOLUSDT",
    "interval": "1d",
    "start_str": "2023-01-01",
    "end_str": "2023-12-31",
    "ma_window": 20,
    "gpt_prompt": "Please provide investment recommendations based on the following data:"
}
```

### Response:

```json
{
    "recommendation": "Based on the recent performance of Solana (SOL) and the calculated moving average, it is advisable to closely monitor the market for potential buy opportunities if the price dips below the 20-day moving average. Historically, buying during such dips has yielded positive returns. However, be cautious of potential market volatility and set appropriate stop-loss limits to mitigate risks. Consider diversifying your investment to spread risk across different assets."
}
```

## Files

- **app/__init__.py**: Initializes the Flask application.
- **app/api.py**: Defines the API routes and handles requests.
- **app/binance_client.py**: Interacts with the Binance API.
- **app/data_processor.py**: Processes the cryptocurrency data.
- **app/gpt_service.py**: Sends data to GPT-3 and retrieves recommendations.
- **app/main.py**: Main application logic.
- **Dockerfile**: Builds the Flask application image.
- **requirements.txt**: Python dependencies.
- **docker-compose.yml**: Docker Compose configuration for multi-container setup.
- **nginx.conf**: Nginx configuration for reverse proxy.
- **run.py**: Entry point for running the Flask application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/)
- [Binance API](https://binance-docs.github.io/apidocs/spot/en/)
- [OpenAI GPT-3](https://beta.openai.com/)

```

This `README.md` file provides an overview of the project, setup instructions, API details, and other relevant information. Make sure to replace placeholders like `https://github.com/AhmedSHelmi/cryptoinsights.git` with actual values if necessary.