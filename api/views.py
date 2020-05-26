from rest_framework.decorators import api_view
from rest_framework.views import Response

from algorithms.tree import get_tree_from_distance_matrix, get_tree_from_similarities

@api_view(["POST"])
def get_tree_using_similarities(request):

    similarities = request.data["similarities"]
        
    tree = get_tree_from_similarities(similarities)

    return Response({"tree": tree})


@api_view(["POST"])
def get_tree_using_distance_matrix(request):

    spieces = request.data["spieces"]
    distance_matrix = request.data["distance_matrix"]

    tree = get_tree_from_distance_matrix(spieces, distance_matrix)

    return Response({"tree": tree})
