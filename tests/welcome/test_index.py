from src.welcome import getMessage


def test_getMessage() -> None:
    expected_message = "Welcome!"
    assert (
        getMessage() == expected_message
    ), f"Expected '{expected_message}', but got '{getMessage()}'"
