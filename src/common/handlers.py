import falcon
import json


class ExceptionHandler:

    def handle_404(req, resp):
        """
              :param req: the request object
              :param resp: the response object
              :return:
        """
        resp.status = falcon.HTTP_404

        message = {
            'error': 'not found: Path=' + req.path,
            'status': 404,
            'title': 'No resource found for your request. Please verify your request.',
            'data': {}
        }
        resp.body = json.dumps(message)

    @staticmethod
    def handle_500(ex, req, resp, params):
        """

        :param ex: the exception catches which allows to launch the method
        :param req: the request object
        :param resp: the response object
        :param params: parameter sending to this method
        :return:
        """
        resp.status = falcon.HTTP_500

        message = {
            'error': 'Something went wrong',
            'status': 500,
            'title': str(ex),
            'data': {}
        }
        resp.body = json.dumps(message)
