import random
import datetime

from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def lotto(request):
    print(request)
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1,46), 6))
    # 값을 딕셔너리에 담아서(보통 context라고 부름)
    context = {'numbers' : numbers}
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Djnago에서 활용하는 템플릿 언어는 Django Template Language(DTL)
    return render(request, 'lotto.html', context)

def dinner(request):
    menus = ['갈치조림', '오징어볶음', '낙지젓갈', '응떡', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'menus': menus,
        'users': [],
        'sentence': 'Life is short, You need Python + django!',
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.goolge.com'
        }
    return render(request, 'dinner.html', context)

def cube(request, number):
    context = {
        'number': number,
        'result': number**3,
        'numbers': [1, 2, 3],
        'students': {'지민': '지민!', '은정': '은정!'}
        }
    return render(request, 'cube.html', context)

def about(request, name, age):
    context = {
        'name': name,
        'age': age
        }
    return render(request, 'about.html', context)