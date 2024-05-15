from django.shortcuts import render

def home(request):
    result = None  # Initialize result with a default value
    try:
        if request.method == 'POST':
            v1 = request.POST.get('value1')
            v2 = request.POST.get('value2')
            operator = request.POST.get('operator')


            if v1.isdigit() and v2.isdigit():
                v1 = int(v1)
                v2 = int(v2)

                if operator == "+":
                    result = v1 + v2
                elif operator == "-":
                    result = v1 - v2
                elif operator == "/":
                    if v2 != 0:
                        result = v1 / v2
                    else:
                        result = "Error: Division by zero"
                elif operator == "*":
                    result = v1 * v2
                elif operator == "%":
                    if v2 != 0: 
                        result = v1 % v2
                    else:
                        result = "Error: Modulo by zero"
            else:
                result = "Error: Invalid input"

    except Exception as e:
        print(e)

    return render(request, 'home.html', {"result": result})