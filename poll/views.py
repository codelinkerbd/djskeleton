from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question, Choice
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from poll.forms import QuestionForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class DetailView(generic.DetailView):
    model = Question
    template_name = "poll/detail.html"
    context_object_name = "question"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "poll/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "poll/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))


class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = "latest_question_list"
    paginate_by = 20

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")


class CreateView(generic.CreateView):
    model = Question
    template_name = 'ca/poll/create.html'
    form_class = QuestionForm
    permission_classes = ["is_authenticated"]


class PollUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Question
    template_name = 'ca/poll/edit.html'
    form_class = QuestionForm
    context_object_name = "obj"
    permission_classes = ["is_authenticated", "is_superuser"]


class PollDeleteView(generic.DeleteView):
    model = Question
    # template_name = 'ca/poll/delete.html'
    success_url = reverse_lazy('poll:index')





