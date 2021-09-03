from django.shortcuts import render


# Create your views here.

def calculator(request, first, do, second):
    print(first, do, second)
    print(do == '-')
    if do == '+':
        return render(request, 'calculator.html', {'res': first + second})
    elif do == '-':
        return render(request, 'calculator.html', {'res': first - second})
    elif do == '*':
        return render(request, 'calculator.html', {'res': first * second})
    elif do == '%':
        try:
            res = first / second
        except ZeroDivisionError as e:
            print(e)
            return render(request, 'calculator.html', {'res': 'НА НОЛЬ ДЕЛИТЬ НЕ ЛЬЗЯ!!!'})
        else:
            return render(request, 'calculator.html', {'res': res})


info = ['пример: 127.0.0.1:8000/calclator/12/-/6', '+ - добавить', '- - отнять', '* - множыть', '% - делить']


def start(request):
    return render(request, 'start.html', {'info': info})
