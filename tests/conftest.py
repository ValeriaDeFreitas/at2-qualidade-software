import socket
import subprocess
import sys
import time
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


def _porta_livre(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) != 0


@pytest.fixture(scope="session")
def live_server():
    """Sobe o Uvicorn numa thread/processo separado para testes E2E."""
    host, port = "127.0.0.1", 8000

    # Se já houver algo rodando na porta, reaproveita (ex.: dev server).
    if not _porta_livre(host, port):
        yield f"http://{host}:{port}"
        return

    proc = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "atividade_qts1.main:app",
            "--host",
            host,
            "--port",
            str(port),
            "--log-level",
            "warning",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Espera a porta abrir (até ~10s).
    for _ in range(100):
        if not _porta_livre(host, port):
            break
        time.sleep(0.1)
    else:
        proc.terminate()
        proc.wait()
        pytest.fail("Servidor Uvicorn não subiu na porta 8000 a tempo.")

    yield f"http://{host}:{port}"

    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()