from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView


class UserReviewsView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user_reviews.html"
    context_object_name = "product_ratings"

    def get_context_data(self, **kwargs: Any) -> Any:
        user = self.request.user
        object_list = user.productrating_set.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context
