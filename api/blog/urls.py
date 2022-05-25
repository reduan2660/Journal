from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt

from blog.schema import schema
import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = bool(os.getenv('DEBUG', 'False').lower() in ('true', '1', 't', 'True'))

urlpatterns = [
    path("", jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))),
    # path("blog", jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))),
    # path("comment", jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))),
]