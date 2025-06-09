"""
Test module for IPPanel Python SDK.
"""
import unittest
from unittest.mock import patch
from ippanel import Client


class TestIPPanelClient(unittest.TestCase):
    """Test cases for IPPanel Client."""

    def setUp(self):
        """Set up test client."""
        self.client = Client("test_api_key")

    def test_init(self):
        """Test client initialization."""
        self.assertEqual(self.client.api_key, "test_api_key")
        self.assertEqual(self.client.base_url, Client.DEFAULT_BASE_URL)

    @patch("requests.Session.post")
    def test_send_webservice(self, mock_post):
        """Test send_webservice method."""
        # Configure the mock
        mock_response = mock_post.return_value
        mock_response.json.return_value = {"data": {}, "meta": {"status": True}}

        # Call the method
        response = self.client.send_webservice(
            message="Test message",
            sender="1000",
            recipients=["09123456789"]
        )

        # Verify the result
        self.assertEqual(response, {"data": {}, "meta": {"status": True}})

        # Verify that the mock was called with the right arguments
        mock_post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
