import io
from unittest.mock import Mock, patch

from src.index import main


def test_main() -> None:
    mock_getMessage = Mock(return_value="Hello, World!")
    with patch("src.index.getMessage", mock_getMessage):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            mock_getMessage.assert_called_once()
            assert mock_stdout.getvalue() == "Hello, World!\n"
