USER_CREATE = {
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "description": "Name of current user",
        },
        "email": {
            "type": "string",
            "pattern": """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
            "description": "Email of current user",
        },

        "password": {
            "type": "string",
            "pattern": "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
            "description": "Password of current user",
        }
    },
    "required": ["username", "email", "password"]
}

AD_CREATE = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of advertisement",
        },
        "description": {
            "type": "string",
            "description": "The text describing the advertisement",
        },
    },
    "required": ["title", "description"]
}
