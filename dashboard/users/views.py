from oscar.apps.dashboard.users.views import (
    IndexView,
    UserDetailView,
)

from .tables import CustomUserTale

class CustomUserListView(IndexView):
    """
    List View for users
    """
    table_class = CustomUserTale


class CustomUserDetailView(UserDetailView):
    """
    Detail View for users
    """
    template_name = 'users/user_detail.html'