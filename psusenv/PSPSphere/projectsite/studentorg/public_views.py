from django.views.generic.list import ListView
from django.utils import timezone
from studentorg.models import Organization, Student, OrgMember


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()

        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values('student')
            .distinct()
            .count()
        )
        context['students_joined_this_year'] = count
        return context
