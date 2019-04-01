import json
import os

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

DATA_DIR = os.path.dirname(__file__) + '/../../data'


class EnglandWeatherView(ViewSet):

    def list(self, request):
        metric = request.query_params['metric']
        start_month = int(request.query_params['start_month'])
        start_year = int(request.query_params['start_year'])
        end_month = int(request.query_params['end_month'])
        end_year = int(request.query_params['end_year'])
        with open(os.path.join(DATA_DIR, metric, 'england/data.json')) as f:
            data = json.loads(f.read())

        filtered_list = [x for x in data if x['month'] in range(start_month, end_month + 1) and (x['year'] == start_year or x['year'] == end_year)]
        return Response(filtered_list)


class ScotlandWeatherView(ViewSet):

    def list(self, request):
        metric = request.query_params['metric']
        start_month = int(request.query_params['start_month'])
        start_year = int(request.query_params['start_year'])
        end_month = int(request.query_params['end_month'])
        end_year = int(request.query_params['end_year'])
        with open(os.path.join(DATA_DIR, metric, 'scotland/data.json')) as f:
            data = json.loads(f.read())

        filtered_list = [x for x in data if x['month'] in range(start_month, end_month + 1) and (x['year'] == start_year or x['year'] == end_year)]
        return Response(filtered_list)
