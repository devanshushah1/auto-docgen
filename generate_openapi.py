import json
from parser import endpoints

spec = {
    "openapi": "3.0.0",
    "info": {
        "title": "My API",
        "version": "1.0.0",
        "description": "Auto-generated spec"
    },
    "servers": [
        {"url": "http://localhost:5000", "description": "Local dev"}
    ],
    "paths": {}
}

for e in endpoints:
    path = e["path"]
    # ensure a dict for this path
    spec["paths"].setdefault(path, {})

    for method in e["methods"]:
        op = {
            "operationId": e["func"],
            "summary": f"{e['func']} handler",
            "responses": {
                "200": {
                    "description": "Successful response",
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"}
                        }
                    }
                }
            }
        }
        spec["paths"][path][method.lower()] = op

# write it out
with open("docs/openapi.json", "w") as f:
    json.dump(spec, f, indent=2)

print("wrote docs/openapi.json")
