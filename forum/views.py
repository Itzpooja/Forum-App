from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Question,Answer,Upvote

def dashboard(request):
	all_question=Question.objects.all()
	all_answer=Answer.objects.all()
	return render(request,"dashboard.html",{"all_question":all_question,"all_answer":all_answer})


def questions(request):
	if request.method == "POST":
		question = request.POST["question"]
		question_instance = Question.objects.create(
			question=question,
			author=request.user
			)
		return redirect("/dashboard/")

	all_question=Question.objects.all().order_by('-timestamp')
	return render(request,"question.html",{"all_question":all_question})

def discussion(request,question_id):
	question=Question.objects.get(pk=question_id)
	if request.method == "POST":
		answer=request.POST["answer"]
		answer_instance=Answer.objects.create(
			answer=answer,
			question=question,
			author=request.user,
			upvotes=1
			)
		return redirect(f"/discussion/{question_id}/")
	all_answer=Answer.objects.filter(question=question_id)
	return render(request,"discussion.html",{"question":question,"answer":all_answer})

def upvote(request,answer_id):
	answer=Answer.objects.get(pk=answer_id)
	upvotes=Upvote.objects.filter(reader=request.user,answer=answer)
	if len(upvotes) == 0:
		answer.upvotes += 1
		answer.save()
		upvote = Upvote(reader=request.user, answer=answer)
		upvote.save()

	return redirect(f"/discussion/{answer.question.id}")

def delete_ques(request, question_id):
	question = Question.objects.get(pk=question_id)
	print(question_id)
	question.delete()

	return redirect("/dashboard/")


def delete_ans(request, answer_id):
	answer = Answer.objects.get(pk=answer_id)
	print(answer_id)
	answer.delete()

	return redirect("/dashboard/")

