# Código da action
import requests
import json
import sys

r = requests.get("https://api.github.com/repos/"+sys.argv[1]+"/"+sys.argv[2]+"/branches", headers={
                 "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})

objeto = json.loads(r.text)

print("\nLista de branches do repositório "+sys.argv[2] + " :")
for v in objeto:
    print(v['name'])
