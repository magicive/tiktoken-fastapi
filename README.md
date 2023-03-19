# Tiktoken API

This API uses the Open AI tiktoken [openai/tiktoken: tiktoken is a fast BPE tokeniser for use with OpenAI's models](https://github.com/openai/tiktoken)  package to encode and decode text.

## Getting Started

To get started, you'll need to have Docker installed on your system. Once you have Docker installed, you can build and run the API using the following commands:

```bash
# Build the Docker image
docker build -t tiktoken-fastapi .

# Run the Docker container
docker run -p 8000:8000 tiktoken-fastapi
```

This will start the API on port 8000.

## API Endpoints

The API provides the following endpoints:

### `/encode`

This endpoint takes a JSON payload containing a `text` field and returns a JSON response containing the encoded text.

#### Request

```json
{
  "text": "Hello, world!"
}
```

#### Response

```json
{
  "encoded_text": [319, 322, 5, 248, 2, 463]
}
```

### `/decode`

This endpoint takes a JSON payload containing an `encoded_text` field and returns a JSON response containing the decoded text.

#### Request

```json
{
  "encoded_text": [319, 322, 5, 248, 2, 463]
}
```

#### Response

```json
{
  "decoded_text": "Hello, world!"
}
```

