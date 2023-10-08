import falcon, json

from src.model.book_model import Book


class BookResource(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        books = Book.objects()

        resp.body = books.to_json()

    def on_post(self, req, resp):

        try:

            resp.status = falcon.HTTP_201
            book_data = req.media

            # req.media will deserialize json object
            book_obj = Book.objects.create(**book_data)
            resp.body = json.dumps({
                'message': 'book successfully created!',
                'status': 201,
                'data': str(book_obj.id)
            })
            return

        except Exception as e:

            resp.status = falcon.HTTP_400
            resp.body = json.dumps({
                'message': str(e),
                'status': 400,
                'data': {}
            })
            return

    def on_get_id(self, req, resp, book_id):
        '''
        :param book_id: book_id received in http path to query book object
        :return:
        '''
        try:
            book_obj = Book.objects.get(id=book_id)

            # Query book collection to get a record with id = book_id
            resp.body = book_obj.to_json()
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.status = falcon.HTTP_404
            resp.body = json.dumps({
                'message': 'Book id does not exist.',
                'status': 404,
                'data': {}
            })
