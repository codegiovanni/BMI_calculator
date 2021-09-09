import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")


def calculate_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get())
    bmi = round(weight / (height ** 2), 1)

    if bmi < 18.5:
        label_result['text'] = f"Underweight: {bmi}"
    elif 18.5 <= bmi <= 24.9:
        label_result['text'] = f"Normal: {bmi}"
    elif 25.0 <= bmi < 29.9:
        label_result['text'] = f"Overweight: {bmi}"
    elif 30.0 <= bmi <= 34.9:
        label_result['text'] = f"Obese: {bmi}"
    else:
        label_result['text'] = f"Extremely obese: {bmi}"


label_weight = tkinter.Label(window, text="Weight (kg): ")
label_weight.grid(column=0, row=0)

entry_weight = tkinter.Entry(window)
entry_weight.grid(column=1, row=0)

label_height = tkinter.Label(window, text="Height (m): ")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(window)
entry_height.grid(column=1, row=1)

label_result = tkinter.Label(window, text="BMI: ")
label_result.grid(column=0, row=2)

button_calculate = tkinter.Button(window, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=1, row=2)

window.mainloop()