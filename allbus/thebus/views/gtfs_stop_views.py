#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ..gtfs_thebus_models import TheBusStop
import json
from ..utilities.thebus.client import parse_xml_to_dict
from ..utilities.thebus.client import TheBusClient
from ..utilities.time.utilities import naive_to_timestamp


def stop_details(request, stop_id, route=None):
    c = TheBusClient(settings.THEBUS_API_CLIENT_TOKEN)
    s = get_object_or_404(TheBusStop, stop_id=stop_id)
    a = c.get_arrivals(int(stop_id), parse_xml_to_dict)

    stopTimes = a.get('stopTimes', None)
    arrivals = stopTimes.get('arrival', None) if stopTimes else None

    if route:
        route = route.upper()
        if arrivals:
            arrivals = filter(lambda x: x['route'] == route, arrivals)

    output = {
        'stop': s.to_dict(),
        'arrivals': arrivals,
        'servertime': stopTimes.get('timestamp')
    }

    try:
        naive_datetime = datetime.datetime.strptime(
            output['servertime'],
            "%m/%d/%Y %I:%M:%S %p")
        output['servertime_ts'] = naive_to_timestamp(
            naive_datetime, tz='Pacific/Honolulu')
    except:
        pass

    if route:
        output['route'] = route

    output['route_names'] = list(TheBusStop.objects.get_route_names(stop_id))

    return HttpResponse(json.dumps(output), mimetype="application/json")


def stop_nearby(request, latitude, longitude):
    stops = TheBusStop.objects.nearby(float(latitude), float(longitude))
    stops_as_json = [s.to_dict() for s in stops] if stops else []
    return HttpResponse(json.dumps(stops_as_json), mimetype="application/json")


# vim: filetype=python
