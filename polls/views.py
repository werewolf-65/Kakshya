from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Question,Choice,Voter
from .forms import QuestionForm,ChoiceForm
from django.urls import reverse
# Create your views here.
def index(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
    # output=", ".join(q.question_text for q in latest_questions)
    # return HttpResponse(output)
    return render(request,"polls/polls_index.html",{'latest_questions':latest_questions})

def detail(request,question_id):
    if(request.method=="POST"):
        form=ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls_index')
    else:
        form=ChoiceForm()
    #question=Question.objects.get(pk=question_id)
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/polls_details.html",{'question':question},{'form':form})
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/polls_results.html",{'question':question})

@login_required
def vote(request,question_id):
    # voters = [user.id for user in Voter.objects.filter(question_id=question_id)]
    q=get_object_or_404(Question,pk=question_id)
    if Voter.objects.filter(question_id=question_id,user_id=request.user.id).exists():
        return render(request,"polls/polls_details.html",{'question':q,"error_message":"You have already voted!"})

    try:
        selected_choice=q.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,"polls/polls_details.html",{'question':q,"error_message":"Please select a choice!"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        v = Voter(user=request.user, question=q)
        v.save()
        return HttpResponseRedirect(reverse('polls_results',args=(q.id, )))

@login_required
def create_poll(request):
    if(request.method=="POST"):
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls_index')
    else:
        form=QuestionForm()
    return render(request,'polls/polls_create.html',{'form':form})

@login_required
def add_options(request,question_id):
    if(request.method=="POST"):
        form=ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls_details',args=(question_id, )))

    else:
        form=ChoiceForm()
    return render(request,'polls/add_options.html',{'form':form})
