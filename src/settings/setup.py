import logging, os, subprocess, sys

def install_external_packages(pacote: str) -> None:

    try:
        os.system("python.exe -m pip install --upgrade pip")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
    except subprocess.CalledProcessError as e:
        raise Exception(f"Erro ao instalar pacote {pacote}: {e}")

def check_packages(pacotes: list) -> None:

    for pacote in pacotes:
        try:
            __import__(pacote)
        except ImportError:
            install_external_packages(pacote)

def initialize_logging():

    from .paths import log_directory    
    
    nome_base = "log_aplicacao"
    logging.basicConfig(
        filename=os.path.join(log_directory, f'{nome_base}.log'),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def check_directories(pastas: list) -> str:

    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
    
    return "Pastas verificadas e criadas, se necessário."
