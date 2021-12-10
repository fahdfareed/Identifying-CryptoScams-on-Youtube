from ctypes import sizeof
import tangram
import PySimpleGUI as sg

model = tangram.Model.from_path('../../../go/scam3.tangram')
# while (1 != 0):
#     output = model.predict({"comment": mycomment})
#     print("Your code is a ", output.class_name)
scam = ""

layout = [[sg.Text("Identifying Scams", font= ("Arial", 25)),],
    [sg.Text("Enter the comment that you want analyzed", text_color = "Black", font = ("Times New Roman", 20))],
    [sg.Text("Comment", font = ("Arial", 15), size = (15,1), key = '-comment'), sg.InputText()],
    [sg.Button("Predict", size= (10,2))],
    [(sg.Text(scam, text_color="Black", font = ("Arial", 15) , size=(100, 4), background_color='white',  key = '-mykey'))],
    
    #[sg.Text(scam, text_color = "Black", font = ("Times New Roman", 18))] ,
    [sg.Button("Don't Show Me Anymore")]]

window = sg.Window("Scam", layout, size=(1200, 800))

    # Closing the window conditions
while True:
    event, values = window.read()
    scam = model.predict({"comment": values[0]}).class_name
    print(scam)
    if event == "Predict":
        if scam == "0":
            scam = "Your comment was not a scam"
        else:
            scam = "Your comment was a scam"
        window[0].update("")
        window['-mykey'].update(scam)

    if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
        break

window.close()