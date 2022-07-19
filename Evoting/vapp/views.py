from dbm import error
from errno import errorcode
import http
from http.client import HTTPResponse
import re
from django.shortcuts import render
from vapp.models import Candidate
from vapp.models import Voter
# Create your views here.

# importing the necessary libraries
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from django.shortcuts import redirect
context=[]
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)

def main(request):
    return render(request, 'main.html')

def trial(request):
    return render(request, 'trial.html')

def connect(request):
    return render(request, 'connect.html')

def vote_verification(request):
    return render(request, 'vote_verification.html')


def vote(request):
    elecCandidates=Candidate.objects.all()
    elecCandidates={'elecCandidates':elecCandidates}
    print(elecCandidates)
    if request.method == 'POST':
        aadharid = request.POST["aid"]

        if Voter.objects.filter(aid=aadharid).exists():
            #return render(request, 'vote.html') 
            if aadharid not in context:
                context.append(aadharid)
                return render(request, 'vote.html',elecCandidates)
            else:
                return HttpResponse("Vote already casted from this ID")
        else:
            return HttpResponse("Aadhar ID not exist..")

def candidate(request):
    if request.method=="POST":
        cid=request.POST.get('cid')
        cname=request.POST.get('cname')
        constituency=request.POST.get('constituency')
        party=request.POST.get('party')
        vcount=request.POST.get('vcount')
        candidate=Candidate(cid=cid,cname=cname,constituency=constituency,party=party,vcount=vcount)
        candidate.save()
    return render(request,'candidate.html')


# Now not in use 

def voter(request):

   if request.method=="POST":
       aid=request.POST.get('aid')
       vname=request.POST.get('vname')
       city=request.POST.get('city')
       voter=Voter(aid=aid,vname=vname,city=city)
       voter.save()
   return render(request,'voter.html')

def entry(request):
    return render(request, 'entry.html') # entry.html renamed as login.html

def login_success(request):
    return render(request, 'select.html')

# def validate(request):
#     if request.method == 'POST':
#         aadharid = request.POST["aid"]

#         if Voter.objects.filter(aid=aadharid).exists():
#             return redirect(vote)
#         else:
#             return HttpResponse("Aadhar ID not exist....")

def vote_count(request):
    if request.method == 'POST':
        selected_candidate = request.POST["candidatesSelect"]
        
        #if (selected_candidate == '1'):
        candidate_update = Candidate.objects.get(cid=selected_candidate)

        candidate_update.vcount = candidate_update.vcount + 1

        candidate_update.save()

        return render(request, "vote_success.html")

def individual_vote_count(request):
    elecCandidates=Candidate.objects.all()
    elecCandidates={'elecCandidates':elecCandidates}
    print(elecCandidates)
    return render(request, 'individual_vote_count.html',elecCandidates)
