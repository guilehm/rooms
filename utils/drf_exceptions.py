import logging

from rest_framework.views import exception_handler

logger = logging.getLogger('rooms')


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    logger.error(
        '\n\tResponse: {exc_code} {exc_text}\n'
        '\tData: {data}\n'
        '\tContext: {context}'.format(
            exc_code=response.status_code,
            exc_text=response.status_text,
            data=response.data,
            context=context,
        )
    )

    return response
