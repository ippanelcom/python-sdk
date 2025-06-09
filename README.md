# IPPanel Python SDK

Official Python client for the [IPPanel SMS API](https://ippanel.com).

## Installation

You can install the package via pip:

```bash
pip install ippanel-python-sdk
```

## Usage

```python
from ippanel import Client

# Initialize the client
client = Client("YOUR_API_KEY")

# Send a simple message via webservice
response = client.send_webservice(
    message="Hello, this is a test message",
    sender="YOUR_SENDER_NUMBER",
    recipients=["RECIPIENT_NUMBER_1", "RECIPIENT_NUMBER_2"]
)
print(response)

# Send a pattern message
response = client.send_pattern(
    pattern_code="YOUR_PATTERN_CODE",
    sender="YOUR_SENDER_NUMBER",
    recipient="RECIPIENT_NUMBER",
    params={
        "name": "John Doe",
        "otp": "12345"
    }
)
print(response)

# Send a voice OTP
response = client.send_votp(
    code=12345,
    recipient="RECIPIENT_NUMBER"
)
print(response)
```

## API Documentation

### Initialization

```python
client = Client(api_key, base_url=None)
```

- `api_key`: Your IPPanel API key
- `base_url` (optional): Custom base URL for the API (defaults to "https://edge.ippanel.com/v1/api")

### Methods

#### Send Web Service Message

```python
client.send_webservice(message, sender, recipients)
```

- `message`: Text message to send
- `sender`: Sender phone number
- `recipients`: List of recipient phone numbers

#### Send Pattern Message

```python
client.send_pattern(pattern_code, sender, recipient, params)
```

- `pattern_code`: The pattern code
- `sender`: Sender phone number
- `recipient`: Recipient phone number
- `params`: Dictionary of parameters for the pattern

#### Send Voice OTP

```python
client.send_votp(code, recipient)
```

- `code`: OTP code (integer or string)
- `recipient`: Recipient phone number

## License

MIT
