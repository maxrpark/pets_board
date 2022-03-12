from .models import Pet, FindMe


def add_variable_to_context(request):
    cvs = Pet.objects.all()[:3]
    findme = FindMe.objects.all()[:3]
    context = {'cvs': cvs, 'findme': findme}
    return context
