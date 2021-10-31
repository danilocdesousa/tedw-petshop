from django.views.generic import TemplateView

# Utilizando a TemplateView para rederização da página.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"
