from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
# 	return HttpResponse('<h1> Hello World </h1>')
	
# def list(request):
# 	return render(request,'list.html')

# def index(request):
# 	Articles = [{'id':1,'titre':'Premier Article','Commentaire':'Télephone Iphone'},
# 		        {'id':2,'titre':'deuxième Article','Commentaire':'Téléphone Samsung '},
# 		        {'id':3,'titre':'troisième Article','Commentaire':'Téléphone HTC'},
# 		        {'id':4,'titre':'quatrième Article','Commentaire':'Téléviseur SONY'},
# 		        {'id':5,'titre':'cinquième Article','Commentaire':'Ecouteur Radio'},
# 	]
# 	return render(request,'index.html', {'Articles' : Articles})
# def home(request):
# 	return render(request,'home.html')
# def contacts(request):
# 	return render(request,'pages/contacts.html')
# def descriptions(request):
# 	return render(request,'pages/descriptions.html')
# def handler404(request):
# 	return render(request,'errors/404.html', {}, status=404)
# def handler500(request):
# 	return render(request,'errors/500.html', {}, status=500)

def home(request):
	return render(request, 'fr/public/home.html')
