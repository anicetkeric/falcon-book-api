import falcon
import pathlib
from falcon_swagger_ui import register_swaggerui_app

import src.common.constants as constants
from src.common.cors import Cors
from src.common.json_translator import JSONTranslator
from src.common.require_json import RequireJSON
import mongoengine as mongo
from src.common.handlers import ExceptionHandler as handler

from src.resource.book_resource import BookResource

mongo.connect(
    constants.MONGO['DATABASE'],
    host=constants.MONGO['HOST'],
    port=constants.MONGO['PORT'],
    username=constants.MONGO['USERNAME'],
    password=constants.MONGO['PASSWORD']
)

STATIC_PATH = pathlib.Path(__file__).parent / 'static'

app = falcon.API(middleware=[Cors(), RequireJSON()])

book = BookResource()
app.add_route('/api/book/', book)
app.add_route('/api/book/{book_id}', book, suffix="id")


app.add_static_route('/static', str(STATIC_PATH))

# global handler exception of application
app.add_error_handler(Exception, handler.handle_500)

# handler for not found resources
app.add_sink(handler.handle_404, '^((?!static).)*$')

register_swaggerui_app(app, constants.SWAGGERUI_URL, constants.SCHEMA_URL, page_title=constants.PAGE_TITLE,
                       favicon_url=constants.FAVICON_URL,
                       config={'supportedSubmitMethods': ['get', 'post', 'put', 'delete'], })
