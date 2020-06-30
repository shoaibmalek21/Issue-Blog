from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm	
from django.contrib import messages
from base.forms import UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from base.models import Post, Agent
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import datetime

def index(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request ,'home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'	
	ordering = ['-date_posted']
	paginate_by = 3

class AgentListView(ListView):
	model = Agent
	template_name = 'agent_details.html'
	context_object_name = 'agents'	
	ordering = ['-id']
	paginate_by = 3

class Agents(ListView):
	model = User
	template_name = 'agents.html'
	context_object_name = 'users'	
	ordering = ['-last_login']
	paginate_by = 10

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account created {username}! You are Go for Login Now.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'auth/register.html', {'form':form})

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AgentInfo(LoginRequiredMixin, CreateView):
	model = Agent
	fields = ['post_id','assigned_to']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AgentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Agent
	fields = ['post_id']

	def form_valid(self, form):
		# form.instance.author = self.request.user
		if form.instance.start_date == None:
			form.instance.start_date = datetime.datetime.now()
		else:
			form.instance.date_commit = datetime.datetime.now()

		forms = super().form_valid(form)
		return forms

	def test_func(self):
		post = self.get_object()
		if self.request.user:
			return True
		return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content','issue']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
