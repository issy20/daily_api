from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Daily


class ListDaily(APIView):
    def get(self, request):
        try:
            daily = Daily.objects.filter(isOpen=True).order_by('-date')
            res_list = [
                {
                    'id': d.id,
                    'date': d.date,
                    'evaluation': d.evaluation.evaluation,
                }
                for d in daily
            ]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DetailDaily(APIView):
    def get(self, request, pk):
        try:
            try:
                daily = Daily.objects.get(id=pk)
            except:
                error_msg = "そんなidの日報はないよ！"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            res = {
                'id': daily.id,
                'date': daily.date,
                'input': daily.input,
                'output': daily.output,
                'question': daily.question,
                'other': daily.other,
                'summary': daily.summary,
            }
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDaily(APIView):
    def get(self, request, cat):
        try:
            daily = Daily.objects.filter(isOpen=True).values_list(
                'date', cat).order_by('-date')
            res_list = [
                {

                    'date': d[0],
                    'content': d[1]
                }
                for d in daily
            ]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
