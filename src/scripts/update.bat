@echo off
chcp 65001 > nul
cd ../../
IF NOT EXIST ".venv" (
    IF NOT EXIST "venv" (
        ECHO Criando ambiente virtual, aguarde ...
        python -m venv .venv
        CALL .venv/Scripts/activate
    ) ELSE (
        CALL venv/Scripts/activate
    )
) ELSE (
    ECHO Ativando ambiente virtual ...
    CALL .venv/Scripts/activate
)
ECHO Atualizando pip ...
python -m pip install --upgrade pip
ECHO Instalando requirements ...
pip install -r requirements.txt
ECHO Atualizando repositório ...
git pull
ECHO Script finalizado ...