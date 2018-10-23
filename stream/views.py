from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import logging

# enable logging in this application
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'stream/index.html')


def stream(request):
    return render(request, 'stream/stream.html')


def list_movies(request):
    return render(request, 'stream/movies.html')