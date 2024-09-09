from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from rest_framework.reverse import reverse_lazy

from products.models import ProductRating


class UserReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductRating
    template_name = "users/user_review_confirm_delete.html"
    success_url = reverse_lazy('my_reviews')

    def get_queryset(self):
        """
        Returns the queryset of ProductRating objects for the current user.
        """
        return ProductRating.objects.filter(user=self.request.user)