from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from elasticsearch import Elasticsearch
from django.shortcuts import render

es = Elasticsearch("http://localhost:9200")


class ProductSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if not query:
            return Response({
                "error": "Query parameter 'q' is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": [
                        "name",
                        "name.autocomplete"
                    ],
                    "fuzziness": "AUTO"
                }
            },
            "highlight": {
                "fields": {
                    "name": {}
                }
            }
        }
        response = es.search(index="products", body=search_body, size=100)
        hits = response['hits']['hits']
        products = []
        for hit in hits:
            product = hit['_source']
            product['id'] = hit['_id']
            if 'highlight' in hit and 'name' in hit['highlight']:
                product['name_highlighted'] = hit['highlight']['name'][0]
            else:
                product['name_highlighted'] = product['name']

            products.append(product)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def product_list_view(request):
    return render(request, "products/product_list.html")