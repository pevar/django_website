from django.views.generic import View, DetailView


class SeoDetailView(DetailView):

    def get_context_data(self, **kwargs):
        context = super(SeoDetailView, self).get_context_data(**kwargs)

        if self.object:
            context['seo'] = self.object.seo()

        return context