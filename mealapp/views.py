from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse
from .import models
import datetime
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from .import models
import datetime
from django.core import serializers
import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os
from django.contrib.auth.decorators import login_required
import hashlib, socket
from django.db.models import Sum
from django.db.models import Q
import numpy as np


def ajax_form(request):
    
    return render(request, 'mealapp/index.html')


def avance_form(request):

    return render(request, 'mealapp/index_advance.html')














































