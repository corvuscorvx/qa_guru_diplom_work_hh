all_city_metro_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      },
      "lines": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "hex_color": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "stations": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "lat": {
                    "type": "number"
                  },
                  "lng": {
                    "type": "number"
                  },
                  "order": {
                    "type": "integer"
                  },
                  "line": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string"
                      },
                      "hex_color": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "hex_color",
                      "name"
                    ]
                  }
                },
                "required": [
                  "id",
                  "name",
                  "lat",
                  "lng",
                  "order",
                  "line"
                ]
              }
            }
          },
          "required": [
            "id",
            "hex_color",
            "name",
            "stations"
          ]
        }
      }
    },
    "required": [
      "id",
      "name",
      "url",
      "lines"
    ]
  }
}

city_metro_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "lines": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "hex_color": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "stations": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "lat": {
                  "type": "number"
                },
                "lng": {
                  "type": "number"
                },
                "order": {
                  "type": "integer"
                },
                "line": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "hex_color": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "hex_color",
                    "name"
                  ]
                }
              },
              "required": [
                "id",
                "name",
                "lat",
                "lng",
                "order",
                "line"
              ]
            }
          }
        },
        "required": [
          "id",
          "hex_color",
          "name",
          "stations"
        ]
      }
    }
  },
  "required": [
    "id",
    "name",
    "lines"
  ]
}

error_metro_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "description": {
      "type": "string"
    },
    "errors": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          }
        },
        "required": [
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
    "errors",
    "request_id"
  ]
}
