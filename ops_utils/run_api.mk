run_api:
	@. ./venv/bin/activate; uvicorn webscraper.api.endpoints:app --host 0.0.0.0 --port 80
