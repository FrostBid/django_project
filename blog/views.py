from django.shortcuts import render

posts = [
	{
		'author': 'Bruh',
		'title': 'Blog post 1',
		'content': 'First blog ever!',
		'date_posted': 'September 9, 2021'
	},
	{
		'author': 'Bruhmomey',
		'title': 'Blog post 2',
		'content': 'Second blog',
		'date_posted': 'September 9, 2021'
	}
]

def home(request):
	context = {
		'posts':posts
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')