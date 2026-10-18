status_code = 301

match status_code:
    case 401 | 403 | 404:
        "Not allowed"
