

from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.template import RequestContext


@xframe_options_exempt
def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = response.json()
    return render(request, 'index.html', {"users": users})


@xframe_options_exempt
def info(request, userid):
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + str(userid))
    user = response.json()
    if user:
        return render(request, 'info.html', {"user": user})
    else:
        return render(request, '404.html', status=404)


@xframe_options_exempt
def posts(request, userid):
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + str(userid))
    user = response.json()
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + str(userid) + '/posts')
    posts = response.json()
    if user:
        return render(request, 'posts.html', {"posts": posts, "user": user})
    else:
        return render(request, '404.html', status=404)


@xframe_options_exempt
def photos(request, userid):
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + str(userid))
    user = response.json()
    response = requests.get('https://jsonplaceholder.typicode.com/photos/')
    photos = response.json()
    response = requests.get('https://jsonplaceholder.typicode.com/albums/')
    albums = response.json()
    photolist = []
    for photo in photos:
        for album in albums:
            if photo["albumId"] == album["id"] and album["userId"] == userid:
                photolist.append(photo)

    if user:
        return render(request, 'photos.html', {"photolist": photolist, "user": user})
    else:
        return render(request, '404.html', status=404)


def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 500
    return response
