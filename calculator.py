def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "خطا! تقسیم بر صفر مجاز نیست."

print("انتخاب کن چه عملیاتی می‌خوای انجام بدی:")
print("1. جمع")
print("2. تفریق")
print("3. ضرب")
print("4. تقسیم")

choice = input("شماره عملیات رو وارد کن (1/2/3/4): ")

num1 = float(input("عدد اول رو وارد کن: "))
num2 = float(input("عدد دوم رو وارد کن: "))

if choice == '1':
    print("نتیجه:", add(num1, num2))
elif choice == '2':
    print("نتیجه:", subtract(num1, num2))
elif choice == '3':
    print("نتیجه:", multiply(num1, num2))
elif choice == '4':
    print("نتیجه:", divide(num1, num2))
else:
    print("ورودی اشتباهه، دوباره تلاش کن!")