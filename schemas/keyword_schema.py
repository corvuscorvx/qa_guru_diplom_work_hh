keyword_search_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    }
                },
                "required": [
                    "text"
                ]
            }
        },
        "suggest_id": {
            "type": "string",
            "format": "uuid"
        }
    },
    "required": [
        "items",
        "suggest_id"
    ]
}

keyword_error_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Generated Schema",
    "type": "object",
    "properties": {
        "description": {
            "type": "string"
        },
        "bad_argument": {
            "type": "string"
        },
        "bad_arguments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "description"
                ]
            }
        },
        "errors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    }
                },
                "required": [
                    "value",
                    "type"
                ]
            }
        },
        "request_id": {
            "type": "string"
        }
    },
    "required": [
        "description",
        "bad_argument",
        "bad_arguments",
        "errors",
        "request_id"
    ]
}
