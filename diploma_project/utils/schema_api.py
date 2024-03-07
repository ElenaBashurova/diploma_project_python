product_create_post_fail = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "method": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "field_error": {
      "type": "string"
    },
    "error": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "method",
    "status",
    "field_error",
    "error",
    "message"
  ]
}

product_create_post = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "method": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "section": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "size": {
          "type": "string"
        },
        "color": {
          "type": "string"
        },
        "params": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "section",
        "description",
        "size",
        "color",
        "params"
      ]
    }
  },
  "required": [
    "method",
    "status",
    "result"
  ]
}

product_info_get = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "method": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "section": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "color": {
          "type": "string"
        },
        "size": {
          "type": "string"
        },
        "price": {
          "type": "number"
        },
        "params": {
          "type": "string"
        },
        "photo": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "section",
        "description",
        "color",
        "size",
        "params",
        "photo"
      ]
    }
  },
  "required": [
    "method",
    "status",
    "result"
  ]
}

product_info_get_fail = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "method": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "field_error": {
      "type": "string"
    },
    "error": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "method",
    "status",
    "field_error",
    "error",
    "message"
  ]
}

product_update_put = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "method": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "result": {
      "type": "string"
    }
  },
  "required": [
    "method",
    "status",
    "result"
  ]
}

product_delete = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "method": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
  },
  "required": [
    "method",
    "status"
  ]
}