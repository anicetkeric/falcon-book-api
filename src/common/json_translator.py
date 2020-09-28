import json
import falcon


class JSONTranslator(object):
    # NOTE: Normally you would simply use req.media and resp.media for
    # this particular use case; this example serves only to illustrate
    # what is possible.

    def process_request(self, req, resp):
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if req.content_length in (None, 0):
            # Nothing to do
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(title='Empty request body',
                                        description='A valid JSON document is required.')

        try:
        
            req.context.doc = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            description = ('Could not decode the request body. The '
                           'JSON was incorrect or not encoded as '
                           'UTF-8.')

            raise falcon.HTTPBadRequest(title='Malformed JSON',
                                        description=description)

    def process_response(self, req, resp, resource, req_succeeded):
        if not hasattr(resp.context, 'result'):
            return

        resp.body = json.dumps(resp.context.result)