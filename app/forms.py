from django.forms import ModelForm

from .models import Pet_CV_Comments, Pet, FindMe, Find_Me_Comments


class Pet_CV_Form(ModelForm):
    class Meta:
        model = Pet_CV_Comments
        exclude = ['pet_cv', 'create_at']


class Create_CV(ModelForm):
    class Meta:
        model = Pet
        # exclude = ['create_at', 'slug']
        fields = "__all__"


class Create_Find_Me(ModelForm):
    class Meta:
        model = FindMe
        # exclude = ['create_at', 'slug']
        fields = "__all__"


class Find_Me_Form(ModelForm):
    class Meta:
        model = Find_Me_Comments
        exclude = ['pet_find_me', 'create_at']
