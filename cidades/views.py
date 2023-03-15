from django.views.generic.list import ListView

from cidades.models import Location

class LocationListView(ListView):

    model = Location
    paginate_by = 25
    template_name = "list_location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search_field')
        return context

    def get_queryset(self):
        queryset = Location.objects.all()
        search = self.request.GET.get('search_field')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset
