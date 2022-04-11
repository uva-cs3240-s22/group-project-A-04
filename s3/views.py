from django.views.generic import View


class HomeView(View):
    template_name = 's3/home.html'

