# Pasta onde o relatório será gerado
$reportPath = ".\coverage"

# Executa o testes e2e
# Executa o testes e2e
py -m pytest --env=local __tests__/.frontend_angular --browser chromium --junitxml=./coverage/frontend_angular_reporter.xml --html=./coverage/frontend_angular_index.html  --no-header
py -m pytest --env=local __tests__/.backend --browser chromium --junitxml=./coverage/backend_reporter.xml --html=./coverage/backend_index.html  --no-header  
py -m pytest --env=local __tests__/.frontend_react --browser chromium --junitxml=./coverage/frontend_react_reporter.xml --html=./coverage/frontend_react_index.html  --no-header 

py .\merge_reports.py

# Encontra o diretório mais recente se for existente
$latestDir = Get-ChildItem -Directory -Path $reportPath | Sort-Object LastWriteTime -Descending | Select-Object -First 1

# Verifica se encontrou um diretório e, em caso afirmativo, obtém o nome do diretório (GUID)
if ($latestDir -ne $null) {

    # Abre a página index.html no navegador padrão do sistema operacional
    Invoke-Item $reportPath\combined_index.html
}
else {
    Write-Host "Nenhum diretório de resultados encontrado."
}

