"""
IPPanel API client for Python.
"""
import json
import requests
from typing import List, Dict, Any, Optional, Union


class Client:
    """IPPanel API client."""

    DEFAULT_BASE_URL = "https://edge.ippanel.com/v1/api"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        """
        Initialize the IPPanel client.

        Args:
            api_key: Your IPPanel API key
            base_url: Optional custom base URL for the API
        """
        self.api_key = api_key
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        })

    def send_webservice(self, message: str, sender: str, recipients: List[str]) -> Dict[str, Any]:
        """
        Send message via webservice.

        Args:
            message: Text message to send
            sender: Sender number
            recipients: List of recipient phone numbers

        Returns:
            API response
        """
        payload = {
            "from_number": sender,
            "message": message,
            "sending_type": "webservice",
            "params": {
                "recipients": recipients
            }
        }
        return self._post("/send", payload)

    def send_pattern(self, pattern_code: str, sender: str, recipient: str,
                     params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a message using a pre-defined pattern.

        Args:
            pattern_code: The pattern code
            sender: Sender number
            recipient: Recipient phone number
            params: Pattern parameters

        Returns:
            API response
        """
        payload = {
            "from_number": sender,
            "recipients": [recipient],
            "code": pattern_code,
            "params": params,
            "sending_type": "pattern"
        }
        return self._post("/send", payload)

    def send_votp(self, code: Union[int, str], recipient: str) -> Dict[str, Any]:
        """
        Send a voice OTP message.

        Args:
            code: OTP code
            recipient: Recipient phone number

        Returns:
            API response
        """
        payload = {
            "message": str(code),
            "sending_type": "votp",
            "params": {
                "recipients": [recipient]
            }
        }
        return self._post("/send", payload)

    def _post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send a POST request to the API.

        Args:
            path: API endpoint path
            payload: Request payload

        Returns:
            API response data

        Raises:
            requests.HTTPError: If the request fails
        """
        url = f"{self.base_url}{path}"

        response = self.session.post(url, json=payload)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses

        return response.json()
