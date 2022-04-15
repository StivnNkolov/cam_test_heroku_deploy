from django.views import generic as generic_views


# TODO to change maybe list views with template views?
class HomeView(generic_views.TemplateView):
    # template_name = 'main_content/index.html'
    template_name = 'main_content/index.html'

