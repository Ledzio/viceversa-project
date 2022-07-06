from django.shortcuts import render

def home(request):
	return render (request, 'home.html')

def reverse(request):
	original_text = request.GET['usertext']
	reversed_text1=original_text[::-1]
	nubmer_of_words = len(original_text.split())
	return render (request, 'reverse.html',{'straight_text':original_text, 'reversed_text':reversed_text1, 'words_number':nubmer_of_words}) 