@echo off
setlocal

rem Salva o caminho do script para poder voltar
set "SCRIPT_DIR=%~dp0"

echo Mudando para o diretorio-raiz do projeto...
cd "%SCRIPT_DIR%../"

rem Inicia a logica de verificacao e limpeza
echo Verificando se estamos dentro da pasta "src"...
for %%I in (.) do set "current_dir_name=%%~nI"

if /i not "%current_dir_name%"=="src" (
    echo ERRO: O script nao conseguiu se mover para a pasta "src".
    pause
    exit /b 1
)

echo Script executado a partir da pasta "src".
echo Deletando pastas __pycache__ recursivamente...

for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        echo Deletando: "%%d"
        rd /s /q "%%d"
    )
)

pause
endlocal