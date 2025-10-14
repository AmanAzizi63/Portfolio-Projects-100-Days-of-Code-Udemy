from tkinter import Tk, ttk
import time
import random

root = Tk()
root.geometry('1000x600')
root.title('WPM tracker')
root.config()

random_texts = [
    "Die Sonne schien warm auf die Wiese, während die Kinder fröhlich spielten und die Vögel in den Bäumen sangen. Es war ein perfekter Tag, um draußen zu sein und die Natur zu genießen.",
    "Technologie entwickelt sich ständig weiter und beeinflusst unser tägliches Leben auf vielfältige Weise. Computer, Smartphones und das Internet sind aus unserem Alltag nicht mehr wegzudenken.",
    "Im Herbst färben sich die Blätter der Bäume in leuchtenden Farben und fallen langsam zu Boden. Spaziergänge durch den Park werden zu einem besonderen Erlebnis, wenn die Luft frisch und klar ist."
]

title = ttk.Label(master=root, text='WPM Tracker', font=('Arial',30, 'normal'))
title.grid(row=1, column=2, pady=5)

guide = ttk.Label(master=root, text='Um deinen WPM Zeit messen zu können musst du den Start Knopf drücken, \n den oberen text abschreiben und dann den Stop Knopf drücken')
guide.grid(row=2, column=2)

text = ttk.Label(master=root, text='Lorem Ipsum si dolor amet', background='#768472', foreground='#FFFFFF', wraplength=800, anchor='center')
text.grid(column=2, row=3, pady=5,  columnspan=2, padx=5)


entry = ttk.Entry(master=root, state='disabled', width=30)
entry.grid(row=5, column=2, pady=5)

starting_time = None

def start():
    global starting_time
    entry.config(state='normal')
    text.config(text=random.choice(random_texts))
    starting_time = time.time()
    print(starting_time)

ending_time = None
time_difference = None
def end():
    global ending_time, time_difference
    if entry.get() == text.cget('text'):
        ending_time = time.time()
        time_difference = ending_time - starting_time
        wordcount = len(entry.get().split())
        wpm = (wordcount/time_difference) * 60
        resultLabel.config(text=f'Dein WPM Wert liegt bei: {wpm}')
    else:
        resultLabel.config(text=f'Du hast den Text nicht richtig Abgeschrieben Versuche es nochmal')
    


endButton = ttk.Button(text='Stop', master=root, command=end)
endButton.grid(row=5, column=3)

startButton = ttk.Button(text='Start', master=root, command=start)
startButton.grid(row=4, column=2, pady=5)



wpm = 0
resultLabel = ttk.Label(master=root, text='Your Result: /')
resultLabel.grid(row=6, column=2, pady=5)

root.mainloop()

