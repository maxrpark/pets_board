from django.shortcuts import get_object_or_404, render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


# import cloudinary.uploader
import cloudinary


from .models import Pet, FindMe
from .forms import Pet_CV_Form, Create_CV, Create_Find_Me, Find_Me_Form


def index(request):
    # pets = Pet.objects.all()
    # context = {'pets': pets}
    return render(request, 'app/index.html')


class HomeView(View):
    def get(self, request):
        cvs = Pet.objects.all()[:3]
        findme = FindMe.objects.all()[:3]
        context = {'cvs': cvs, 'findme': findme}
        return render(request, 'app/index.html', context)


class FindMeView(View):
    def get(self, request):
        pets = FindMe.objects.all()
        context = {'pets': pets}
        return render(request, 'app/find_me.html', context)


class FindMePet(View):
    def get(self, request, slug):
        pet = get_object_or_404(FindMe, slug=slug)
        context = {
            "pet": pet,
            "comments_form": Find_Me_Form(),
            "comments": pet.comments.all().order_by('-id')

        }
        return render(request, 'app/find_me_pet.html', context)

    def post(self, request, slug):
        comment_form = Find_Me_Form(request.POST)
        pet = FindMe.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.pet_find_me = pet
            comment.save()
            return HttpResponseRedirect(reverse('find-me-pet', args=[slug]))

        context = {
            "pets": pet,
            "comments_form": comment_form,
            "comments": pet.comments.all().order_by('-id')
        }
        return render(request, 'app/find_me_pet.html', context)


class Create_Find_Me_View(View):
    def get(self, request):
        context = {
            "comments_form": Create_Find_Me(),
        }
        return render(request, 'app/create_find_me.html', context)

    def post(self, request):
        comment_form = Create_Find_Me(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect('/find-me')
        else:
            print('Nooooo')
            context = {
                "comments_form": comment_form,
            }
            return render(request, 'app/create_find_me.html', context)


# CV

class All_CVs(View):
    def get(self, request):
        pets = Pet.objects.all()
        context = {'pets': pets}
        return render(request, 'app/cvs.html', context)


class PetCV(View):
    def get(self, request, slug):
        pet = Pet.objects.get(slug=slug)

        context = {
            'pet': pet,
            "comments_form": Pet_CV_Form(),
            "comments": pet.comments.all().order_by('-id')
        }
        return render(request, 'app/pet_cv.html', context)

    def post(self, request, slug):
        comment_form = Pet_CV_Form(request.POST)
        pet = Pet.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.pet_cv = pet
            comment.save()
            return HttpResponseRedirect(reverse('pet_cv', args=[slug]))

        context = {
            "pets": pet,
            "comments_form": comment_form,
            "comments": pet.comments.all().order_by('-id')
        }
        return render(request, 'app/pet_cv.html', context)


class Create_CV_View(View):
    def get(self, request):
        context = {
            "comments_form": Create_CV(),
        }
        return render(request, 'app/create_cv.html', context)

    def post(self, request):
        comment_form = Create_CV(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.save()

            return HttpResponseRedirect('/')
        else:
            print('Nooooo')
            context = {
                "comments_form": comment_form,
            }
            return render(request, 'app/create_cv.html', context)


class showResults(View):
    def get(self, request, section, slug):
        if section == 'cvs':
            pets = Pet.objects.all()
            cvs = pets.filter(Q(sex=slug) | Q(
                neutered=slug) | Q(size=slug))
            context = {'cvs_result': cvs, "section": section, "query": slug}
        elif section == 'findme':
            find_me_all = FindMe.objects.all()
            findme = find_me_all.filter(Q(sex=slug) | Q(
                neutered=slug) | Q(size=slug))
            context = {'findme_result': findme,
                       "section": section, "query": slug}
        return render(request, 'app/results.html', context)

    def get(self, request):
        query = request.GET.get('query', '')
        pets = Pet.objects.all()
        cvs = pets.filter(
            Q(name__iexact=query) | Q(sex__iexact=query))
        find_me_all = FindMe.objects.all()
        findme = find_me_all.filter(
            Q(name__iexact=query) | Q(sex__iexact=query))
        print(findme)
        context = {'cvs_result': cvs, 'findme_result': findme,  "query": query}
        return render(request, 'app/results.html', context)
