from pyscript import document, when

class Racer:
    def __init__(self, name, horse, racer_no):
        self.name = name
        self.horse = horse
        self.racer_no = racer_no

    def introduce(self):
        return f"{self.name}, riding {self.horse}. Number: {self.racer_no}."


racers = [
    Racer("Gyro Zeppeli", "Valkyrie", "636"),
    Racer("Johnny Joestar", "Slow Dancer", "939"),
    Racer("Diego Brando", "Silver Bullet", "001"),
    Racer("Pocoloco", "Fame-Hungry", "777"),
    Racer("Sandman", "None", "990")
]


@when("click", "#addBtn")
def add_racer(event):
    name = document.getElementById("name").value
    horse = document.getElementById("horse").value
    racer_no = document.getElementById("racer_no").value

    if name and horse and racer_no:
        racers.append(Racer(name, horse, racer_no))

        document.getElementById("name").value = ""
        document.getElementById("horse").value = ""
        document.getElementById("racer_no").value = ""


@when("click", "#showBtn")
def show_list(event):
    output_div = document.getElementById("output")
    output_div.innerHTML = ""

    for r in racers:
        output_div.innerHTML += f"<p>{r.introduce()}</p>"