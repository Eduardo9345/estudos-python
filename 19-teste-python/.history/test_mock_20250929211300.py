import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    """
    
    Fixture que retorna um objeto de resposta mockado com status code 200 e um
    corpo JSON específico
    
    """
    
    mock = MagicMock()
    