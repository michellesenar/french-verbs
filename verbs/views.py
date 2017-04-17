import random

from django.shortcuts import render

from . import models

PRONOUNS = [
        ('I', 'je'),
        ('you', 'tu'),
        ('he', 'il'),
        ('she', 'elle'),
        ('we', 'nous'),
        ('you guys', 'vous'),
        ('they', 'ils'),
        ('they', 'elles'),
]


def home(request):
    return render(request, 'verbs/home.html', {})


def randomizer(request):
    random_pk = random.randint(1, 740)
    random_verb = models.FrenchVerb.objects.get(id=random_pk)
    english = random_verb.english

    possible_answers = models.FrenchVerb.objects.filter(english=english).all()
    return render(request, 'verbs/randomizer.html', {'random_verb':
        random_verb, 'possible_answers': possible_answers})


def about(request):
    return render(request, 'verbs/about.html', {})


def conjugation(request, verb_pk):
    verb = models.FrenchVerb.objects.get(id=verb_pk)
    BASE_URL = 'http://www.wordreference.com/conj/FrVerbs.aspx?v={}'
    verb_url = BASE_URL.format(verb.french)

    pronoun = random.choice(PRONOUNS)
    return render(request, 'verbs/conjugation.html', {'pr': pronoun, 'verb': verb, 'verb_url':
        verb_url})

