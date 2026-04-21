from pyscript import document, when

# this is a class for each racer in the list
class Racer:
    def __init__(self, name, horse, racer_no):
        # store racer information
        self.name = name
        self.horse = horse
        self.racer_no = racer_no

    # format for each racer
    def introduce(self):
        return f"{self.name}, riding {self.horse}. Number: {self.racer_no}."


# list of racers
racers = [
    Racer("Gyro Zeppeli", "Valkyrie", "636"),
    Racer("Johnny Joestar", "Slow Dancer", "939"),
    Racer("Diego Brando", "Silver Bullet", "001"),
    Racer("Pocoloco", "Fame-Hungry", "777"),
    Racer("Sandman", "None", "990")
]


# works when "Add Racer" is clicked
@when("click", "#addBtn")
def add_racer(event):

    # get values from the input boxes in HTML
    name = document.getElementById("name").value
    horse = document.getElementById("horse").value
    racer_no = document.getElementById("racer_no").value

    # check if all inputs are filled
    if name and horse and racer_no:

        # add new racer to the list
        racers.append(Racer(name, horse, racer_no))

        # clear input fields after adding
        document.getElementById("name").value = ""
        document.getElementById("horse").value = ""
        document.getElementById("racer_no").value = ""


# works when "Show List" is clicked
@when("click", "#showBtn")
def show_list(event):

    # get the output box in HTML
    output_div = document.getElementById("output")

    # clear previous output so it doesn't repeat
    output_div.innerHTML = ""

    # loop through all racers and display them
    for r in racers:
        output_div.innerHTML += f"<p>{r.introduce()}</p>"
