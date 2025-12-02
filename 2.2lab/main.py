import math

def TypeTrl(x1,y1,x2,y2,x3,y3):
    a = ((x2-x1)**2 + (y2-y1)**2)**0.5
    b = ((x3-x2)**2 + (y3-y2)**2)**0.5
    c = ((x1-x3)**2 + (y1-y3)**2)**0.5
    
    s = sorted([a,b,c])
    if s[0]+s[1] <= s[2]:
        return "Не треугольник"
    
    
    eq = abs(a-b)<0.001 or abs(b-c)<0.001 or abs(c-a)<0.001
    rt = abs(s[0]**2 + s[1]**2 - s[2]**2) < 0.001
    
    
    if abs(a-b)<0.001 and abs(b-c)<0.001:
        return "Равносторонний"
    elif eq and rt:
        return "Прямоугольный равнобедренный"
    elif eq:
        return "Равнобедренный"
    elif rt:
        return "Прямоугольный"
    else:
        return "Обычный"
