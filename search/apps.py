import oscar.apps.search.apps as apps
from oscar.core.loading import get_class

class SearchConfig(apps.SearchConfig):
    name = 'search'

    def ready(self):
        super(SearchConfig, self).ready()
        self.search_view = get_class('search.views', 'CustomFacetedSearchView')
