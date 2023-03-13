from django.shortcuts import render



def midterm_a(request):
    context = {
        'jobroles': ['reporting executive', 'business analyst',
                     'data analyst', 'statistician', 'data scientist',
                     'data engineer/data architect', 'machine learning engineer',
                     'big data engineer']
    }


    return render(request,'midterma.html',context)
