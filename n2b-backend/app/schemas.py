import simplejson
import marshmallow as msh

class WineReviewSchema(msh.Schema):
    country = msh.fields.Str()
    description = msh.fields.Str()
    points = msh.fields.Int()
    price = msh.fields.Decimal()
    variety = msh.fields.String()

class Pagination(msh.Schema):
    page = msh.fields.Int()

class FilterSchema(msh.Schema):
    filter_data = msh.fields.Nested(WineReviewSchema, default={})
    page = msh.fields.Int(default=1)

class SearchResultSchema(msh.Schema):
    country = msh.fields.Str()
    description = msh.fields.Str()
    points = msh.fields.Int()
    price = msh.fields.Decimal()
    variety = msh.fields.String()

    class Meta:
        json_module = simplejson