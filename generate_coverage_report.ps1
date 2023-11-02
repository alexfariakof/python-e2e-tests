# Pasta onde o relatório será gerado
$reportPath = ".\coverage"

# Executa o testes e2e
pytest --browser chromium  --junitxml=./coverage/pytest_reporter.xml --html=./coverage/index.html     

# Encontra o diretório mais recente se for existente
$latestDir = Get-ChildItem -Directory -Path $reportPath | Sort-Object LastWriteTime -Descending | Select-Object -First 1

# Verifica se encontrou um diretório e, em caso afirmativo, obtém o nome do diretório (GUID)
if ($latestDir -ne $null) {

    # Abre a página index.html no navegador padrão do sistema operacional
    Invoke-Item $reportPath\index.html
}
else {
    Write-Host "Nenhum diretório de resultados encontrado."
}

