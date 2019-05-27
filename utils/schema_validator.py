import json

from jsonschema import validate


def schema_validation(schema_name, request):
    with open('./data/schemas/' + schema_name, 'r') as f:
        schema_data = f.read()
    schema = json.loads(schema_data)
    return bool(validate(request, schema))
