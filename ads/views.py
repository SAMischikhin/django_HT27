from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ads
import json


class Index(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ViewCat(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories()
        category.name = category_data["name"]

        try:
            category.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        category.save()
        return JsonResponse({
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class ViewAd(View):
    def get(self, request):
        items = Ads.objects.all()
        response = []
        for item in items:
            response.append({
                "id": item.id,
                "name": item.name,
                "author": item.author,
                "price": item.price
            })
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ads_data = json.loads(request.body)

        item = Ads()
        item.name = ads_data["name"]
        item.author = ads_data["author"]
        item.price = ads_data["price"]
        item.address = ads_data["address"]
        item.description = ads_data["description"]

        try:
            item.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        item.save()
        return JsonResponse({
            "id": item.id,
            "name": item.name
        })


class CatDetailView(DetailView):
    model = Categories

    def get(self, *args, **kwargs):
        try:
            category = self.get_object()
            return JsonResponse({
                'id': category.id,
                'name': category.name
            })
        except Http404:
            return JsonResponse({'Error': '404'}, status=404)


class AdDetailView(DetailView):
    model = Ads

    def get(self, *args, **kwargs):
        try:
            item = self.get_object()
            return JsonResponse({
                "id": item.id,
                "name": item.name,
                "author": item.author,
                "price": item.price,
                "description": item.description,
                "address": item.address,
                "is_published": item.is_published
            })
        except Http404:
            return JsonResponse({'Error': '404'}, status=404)
