from rest_framework.response import Response


def quick_success_response(status_code, message):
    '''
    Quick success response.

    @param: satus_code (int): HTTP status code.
    @param: message (str): Message to return.

    :returns:
        Response: Response object.
    '''
    return Response(
        {
            'status': status_code,
            'message': message
        },
        status=status_code
    )


def quick_error_response(status_code, message):
    '''
    Quick error response.

    @param: satus_code (int): HTTP status code.
    @param: message (str): Message to return.

    :returns:
        Response: Response object.
    '''
    return Response(
        {
            'status': status_code,
            'message': message
        },
        status=status_code
    )
