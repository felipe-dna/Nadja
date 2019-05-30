from django.views.generic import TemplateView


# View Bellow


class HomeView(TemplateView):
    template_name = 'core/home.html'
