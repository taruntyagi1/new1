from oscar.apps.search.views import FacetedSearchView

class CustomFacetedSearchView(FacetedSearchView):
    """
    Customized Search View
    """

    template = "search/results.html"