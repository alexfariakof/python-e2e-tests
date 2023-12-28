from bs4 import BeautifulSoup
import junitparser


# Caminhos para os relatórios individuais
report_paths = [
    './coverage/frontend_angular_reporter.xml',
    './coverage/backend_reporter.xml',
    './coverage/frontend_react_reporter.xml',
]

html_paths = [
    './coverage/backend_index.html',
    './coverage/frontend_angular_index.html',    
    './coverage/frontend_react_index.html',
]

# Caminho para o relatório combinado
combined_report_path = './coverage/combined_reporter.xml'
combined_html_path = './coverage/combined_index.html'

# Mesclar relatórios XML
combined_suite = junitparser.JUnitXml()
for path in report_paths:
    suite = junitparser.JUnitXml.fromfile(path)
    combined_suite += suite

# Salvar o relatório combinado XML
combined_suite.write(combined_report_path)

# Combinação de conteúdo HTML
with open(combined_html_path, 'w') as combined_html:
    # Adiciona a estrutura inicial do HTML
    combined_html.write('<html><head></head><body>')

    for html_path in html_paths:
        with open(html_path, 'r') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            
            combined_html.write(str(soup))

    # Adiciona a estrutura final do HTML
combined_html.write('</body></html>')
