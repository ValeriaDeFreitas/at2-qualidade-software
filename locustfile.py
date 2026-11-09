import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

root_dir = Path(__file__).resolve().parent.parent
src_dir = root_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from atividade_qts1.main import app  # noqa: E402


@pytest.fixture
def client():
    print("\n[SETUP] A iniciar TestClient do FastAPI...")
    c = TestClient(app)
    yield c
    print("\n[TEARDOWN] A encerrar TestClient...")