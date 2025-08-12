import os
from parser import endpoints
from docgen import hf_query

os.makedirs("docs", exist_ok=True)
with open("docs/openapi.json","w") as out:
    out.write("# API Reference\n\n")
    for e in endpoints:
        prompt = f"""
Write swagger-style openapi.json format for this endpoint. No other content Just the json for this endpoint that can directly go into a .json file
operationId: {e['func']}
method: {e['methods'][0]}
path: {e['path']}

include a short description and example curl
"""
        docs = hf_query(prompt)
        out.write(docs)
        out.write("\n\n---\n\n")
print("wrote docs/openapi.json")