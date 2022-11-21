# oscar imports
import oscar.apps.dashboard.users.apps as apps
from oscar.core.loading import get_class

from django.conf.urls import url

class UsersDashboardConfig(apps.UsersDashboardConfig):
    name = 'dashboard.users'

    def ready(self):
        super(UsersDashboardConfig, self).ready()
        from .views import (
            CustomUserListView,
            CustomUserDetailView,
        )
        self.index_view = CustomUserListView
        self.user_detail_view = CustomUserDetailView
