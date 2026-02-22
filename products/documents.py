from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from products.models import Product
from elasticsearch_dsl import analyzer, token_filter

autocomplete_analyzer = analyzer(
    'autocomplete_analyzer',
    tokenizer='standard',
    filter=[
        'lowercase',
        token_filter('autocomplete_filter', 'edge_ngram', min_gram=1, max_gram=20)
    ]
)


@registry.register_document
class ProductDocument(Document):
    name = fields.TextField(
        attr='name',
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'autocomplete': fields.TextField(analyzer=autocomplete_analyzer),
        }
    )
    brand = fields.TextField(
        attr='brand',
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'autocomplete': fields.TextField(analyzer=autocomplete_analyzer),
        }
    )
    price = fields.TextField(
        attr='price',
        fields={
            'raw': fields.DoubleField(),
            'autocomplete': fields.TextField(analyzer=autocomplete_analyzer),
        }
    )

    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Product
        fields = []