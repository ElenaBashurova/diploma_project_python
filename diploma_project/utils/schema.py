item_post_fail = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "message": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "success",
    "message"
  ]
}

item_post = ({
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "message": {
            "type": "string"
        },
        "updatetopcartsectionhtml": {
            "type": "string"
        },
        "updateflyoutcartsectionhtml": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "message",
        "updatetopcartsectionhtml",
        "updateflyoutcartsectionhtml"
    ]
}
)
