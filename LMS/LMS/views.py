from django.contrib import messages
from django.shortcuts import redirect, render
from app.models import Course, Categories, Level, Video, UserCourse, QuesModel, Quiz
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum


def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('id')
    print(course)
    context = {
        'category': category,
        'course': course,
    }
    return render(request, 'Main/home.html', context)


def SINGLE_COURSE(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    context = {
        'category': category,
        'level': level,
        'course': course,
    }
    return render(request, 'Main/single_course.html', context)


def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    if category:
        course = Course.objects.filter(category__id__in=category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in=level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')
    context = {
        'course': course
    }
    t = render_to_string('ajax/course.html', context)
    return JsonResponse({'data': t})


def CONTACT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }

    return render(request, 'Main/contact_us.html', context)


def ABOUT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request, 'Main/about_us.html', context)


def SEARCH_COURSE(request):
    category = Categories.get_all_category(Categories)
    query = request.GET['query']
    course = Course.objects.filter(title__icontains=query)

    context = {
        'course': course,
        'category': category
    }
    return render(request, 'search/search.html', context)


def COURSE_DETAILS(request, slug):
    category = Categories.get_all_category(Categories)
    time_duration = Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))

    course_id = Course.objects.get(slug=slug)

    quiz = Quiz.objects.all()

    try:
        check_enroll = UserCourse.objects.get(user=request.user, course=course_id)
    except UserCourse.DoesNotExist:
        check_enroll = None
    course = Course.objects.filter(slug=slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {
        'course': course,
        'category': category,
        'time_duration': time_duration,
        'check_enroll': check_enroll,
        'quiz': quiz
    }
    return render(request, 'course/course_detail.html', context)



def QUIZ(request):
    # Quiz.objects.get(slug=slug)


    # weight = QuesModel.get_all_questions(QuesModel)
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score+=10
                correct+=1

            else:
                wrong+=1

        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request,'quiz/quiz.html',context)
def mark(entity):
    # Custom logic to determine the marking condition
    # Modify this function according to your requirements

    # Example: Check if the entity's course title contains "Physics"
    # Return True if it does, False otherwise
    if entity.course.title.lower().find("Python") != -1:
        return True
    else:
        return False

def getAchLevels(e):
    e.ach = 0  # Initialize achievement level for the current node
    if not isinstance(e, QuesModel):  # If e is not an assessment tool
        e.ach = 0

    for d in e.get_descendants():
        if mark(e) != mark(d):
            getAchLevels(d)
        e.ach += d.ach * e.weight

    return e.ach

def calculate_achievement(request):
    roots = QuesModel.objects.filter(
        learnout__isnull=True)  # Assuming you want to calculate achievement for root competencies

    for root in roots:
        getAchLevels(root)

    # You can now access the achievement level of each QuesModel instance
    for ques in QuesModel.objects.all():
        print(f"Question: {ques.question}, Achievement Level: {ques.ach}")

    # Render your view or return an HttpResponse
    return render(request, 'result.html', {'ques_list': QuesModel.objects.all()})


def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category
    }
    return render(request, 'error/404.html', context)


def CHECKOUT(request, slug):
    course = Course.objects.get(slug=slug)

    if course.price == 0:
        course = UserCourse(
            user=request.user,
            course=course,
        )
        course.save()
        messages.success(request, 'Course is successfully enrolled!')
        return redirect('my_course')
    return render(request, 'checkout/checkout.html')


def MY_COURSE(request):
    course = UserCourse.objects.filter(user=request.user)

    context = {
        'course': course,
    }
    return render(request, 'course/my-course.html', context)


def WATCH_COURSE(request, slug):
    return render(request, 'course/watch_course.html')


