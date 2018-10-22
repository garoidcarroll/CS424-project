from django.shortcuts import render
from django.http import HttpResponse
from locations.models import Member


def member(request,member_id):
    member = Member.objects.get(id=member_id)

    return HttpResponse('%s %s'%(member.location_name,member.town_name))
