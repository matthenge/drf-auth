def success_response(code, data, message):
    response = {
        'code': code,
        'data': data,
        'message': message,
    }

    return response


def error_response(code, message, error):
    response = {
        'code': code,
        'message': message,
        'error': error
    }

    return response
