# PII Detection API

The PII Detection API is designed to analyze text paragraphs and identify personally identifiable information (PII) within them using the "dbmdz/bert-large-cased-finetuned-conll03-english" model from Hugging Face's Transformers library. This API takes a text paragraph as input and returns an array of detected PII found in the text.

## Table of Contents

- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Request](#request)
- [Response](#response)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Dependencies](#dependencies)

## Usage

To use the PII Detection API, send a POST request to the `/analyze_pii` endpoint with JSON data containing the text paragraph you want to analyze. The API will respond with an array of detected PII values.

## API Endpoint

- **Base URL**: `http://localhost:5000` (Replace with the actual base URL if deployed elsewhere)

### Analyze PII Endpoint

- **URL**: `/analyze_pii`
- **Method**: POST
- **Request Content-Type**: `application/json`

## Request

The API accepts a JSON request with the following structure:

```json
{
    "body": "Text paragraph to analyze for PII detection."
}
