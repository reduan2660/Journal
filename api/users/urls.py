from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from users.schema import schema
from django.views.decorators.csrf import csrf_exempt

import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = bool(os.getenv('DEBUG', 'False').lower() in ('true', '1', 't', 'True'))

urlpatterns = [
    # Only a single URL to access GraphQL
    path("me", jwt_cookie(GraphQLView.as_view(graphiql=DEBUG, schema=schema))),
]