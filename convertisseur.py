from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

fenetre = Tk()

liste_devise = ["Euro", "Dollar", "Livre", "Yen"]
dict_taux = {"Euro":1.00, "Dollar":1.08, "Livre":0.89, "Yen":139.21}

monnaie_Depart = StringVar(fenetre)
monnaie_Depart.set("Devise")
monnaie_Fin = StringVar(fenetre)
monnaie_Fin.set("Devise")


def Convertir():

    resultat.delete(0, END)

    try:
        somme_depart = float(montant.get())
        somme_finale = (somme_depart*(dict_taux["Euro"]/dict_taux[monnaie_Depart.get()]))*dict_taux[monnaie_Fin.get()]
        resultat.insert(0, f"{somme_finale:.2f}")

        hist = f"{somme_depart:.2f} {monnaie_Depart.get()} = {somme_finale:.2f} {monnaie_Fin.get()}"
        lbl_hist = Label(conv_hist, text=hist)
        lbl_hist.pack()

    except:
        showerror('Erreur Conversion', 'Champ(s) invalide(s)')


def Ajout_Devise():

    try:
        if not dict_taux[nom_devise.get()]:
            
            liste_devise.append(nom_devise.get())
            dict_taux[nom_devise.get()] = float(valeur_devise.get())

            Monnaie1.destroy()
            Monnaie2.destroy()
            
            new_Monnaie1 = OptionMenu(conv_main, monnaie_Depart, *liste_devise)
            new_Monnaie1.config(width=24)
            new_Monnaie1.grid(row=1, column=1)

            new_Monnaie2 = OptionMenu(conv_main, monnaie_Fin, *liste_devise)
            new_Monnaie2.config(width=24)
            new_Monnaie2.grid(row=2, column=1)

    except:
        showerror('Erreur Ajout', 'Champ(s) invalide(s)')


# Menu de conversion

conv_main = LabelFrame(fenetre, text="Convertisseur de monnaie", pady=10)
conv_main.pack(fill="both", expand="yes")

lbl_Montant = Label(conv_main, text="Montant :").grid(row=0, column=0)
montant = Entry(conv_main, width=30)
montant.grid(row=0, column=1)

lbl_Monnaie_init = Label(conv_main, text="De :").grid(row=1, column=0)
Monnaie1 = OptionMenu(conv_main, monnaie_Depart, *liste_devise)
Monnaie1.config(width=24)
Monnaie1.grid(row=1, column=1)

lbl_Monnaie_conv = Label(conv_main, text="A :").grid(row=2, column=0)
Monnaie2 = OptionMenu(conv_main, monnaie_Fin, *liste_devise)
Monnaie2.config(width=24)
Monnaie2.grid(row=2, column=1)

btn_convertir = Button(conv_main, text="Convertir", command=Convertir, width= 25).grid(row=4, column=1, padx=10, pady= 10)

lbl_Resultat = Label(conv_main, text="Resultat").grid(row=5, column=1)
resultat = Entry(conv_main, width=30)
resultat.grid(row=5, column=1)

# Ajout de devises

ajt_devise = LabelFrame(fenetre, text="Ajout de devises", pady=10)
ajt_devise.pack(fill="both", expand="yes")

lbl_nom_devise = Label(ajt_devise, text="Nom :").grid(row=0, column=0)
nom_devise = Entry(ajt_devise, width=30)
nom_devise.grid(row=0, column=1)

lbl_valeur_devise = Label(ajt_devise, text="Taux :").grid(row=1, column=0)
valeur_devise = Entry(ajt_devise, width=30)
valeur_devise.grid(row=1, column=1)

btn_ajout = Button(ajt_devise, text="Ajouter", command=Ajout_Devise, width= 25).grid(row=2, column=1, padx=10, pady= 10)

# Historique des conversions

conv_hist = LabelFrame(fenetre, text="Historique")
conv_hist.pack(fill="both", expand="yes")

fenetre.mainloop()