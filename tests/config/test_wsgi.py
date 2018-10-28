import io
import pytest


@pytest.mark.django_db
def test_application():
    from config.wsgi import application

    # https://www.python.org/dev/peps/pep-0333/#environ-variables
    environ = {
        'REQUEST_METHOD': 'GET',
        'SERVER_NAME': 'server',
        'SERVER_PORT': 80,
        'wsgi.input': io.BytesIO(b''),
    }

    # https://www.python.org/dev/peps/pep-0333/#the-start-response-callable
    def start_response(status, response_headers, exc_info=None):
        pass

    # A dud request is quickly rejected as a bad client request.
    response = application(environ, start_response)
    assert response.status_code == 400
