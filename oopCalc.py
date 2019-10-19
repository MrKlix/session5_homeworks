from oopCalcClasses import Calculator

bedingung = True
zahl1 = 0
zahl2 = 0
op = ""

while bedingung:
    try:
        zahl1 = int(input("Zahl1: ").strip())
        op = input("Welche Rechenart wollen Sie nutzen? (+ | - | / | * | x² | log | wurzel | potenz) ").strip().lower()

        if op in ["log", "wurzel"]:
           calc1 = Calculator(zahl1)
           print(calc1.get_CalcResult(op))
        else:
            zahl2 = int(input("Zahl2: ").strip())

        calc2 = Calculator(zahl1, zahl2)
        print(calc2.get_CalcResult(op))

    except ValueError:
        print("Überprüfen Sie Ihre Eingabe!")

    decision = input("Möchten Sie es erneut versuchen? (ja | nein) : ").strip().lower()
    if decision == "nein":
        bedingung = False