from graphene import Schema

from src.schema.mutation import Mutation
from src.schema.query import Query

schema = Schema(query=Query, mutation=Mutation)
