import simplejson
import marshmallow as msh

class WineReviewSchema(msh.Schema):
    country = msh.fields.Str()
    description = msh.fields.Str()
    points = msh.fields.Int()
    price = msh.fields.Decimal()
    variety = msh.fields.String()

class FilterSchema(msh.Schema):
    filter_data = msh.fields.Nested(WineReviewSchema, default={})
    page = msh.fields.Int()
    page_size = msh.fields.Int()