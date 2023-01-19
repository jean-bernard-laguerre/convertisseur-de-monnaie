from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

fenetre = Tk()
fenetre.title("Convertisseur")

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
        somme_finale = (somme_depart * (dict_taux["Euro"] / dict_taux[monnaie_Depart.get()])) * dict_taux[monnaie_Fin.get()]
        resultat.insert(0, f"{somme_finale:.2f}")

        #Ajout dans l'historique
        conv = f"{somme_depart:.2f} {monnaie_Depart.get()} = {somme_finale:.2f} {monnaie_Fin.get()}"
        lbl_hist = Label(hist, text=conv)
        lbl_hist.pack()

    except:
        showerror('Erreur Conversion', 'Champ(s) invalide(s)')


def Ajout_Devise():

    try:
        #Ajoute la devise si elle n'est pas dans la liste
        if not dict_taux[nom_devise.get()]:
            
            liste_devise.append(nom_devise.get())
            dict_taux[nom_devise.get()] = float(valeur_devise.get())

            Monnaie1.destroy()
            Monnaie2.destroy()
            
            #Nouveau option menu avec liste a jour
            new_Monnaie1 = OptionMenu(conv_main, monnaie_Depart, *liste_devise)
            new_Monnaie1.config(width=24)
            new_Monnaie1.grid(row=1, column=1)

            new_Monnaie2 = OptionMenu(conv_main, monnaie_Fin, *liste_devise)
            new_Monnaie2.config(width=24)
            new_Monnaie2.grid(row=2, column=1)
        
        #Modifie le taux si la devise est presente 
        else:
            dict_taux[nom_devise.get()] = float(valeur_devise.get())

    except:
        showerror('Erreur Ajout', 'Champ(s) invalide(s)')


def suppr_historique():
    for element in hist.winfo_children():
        element.destroy()


# Menu de conversion

conv_main = Frame(fenetre, pady=10)
conv_main.pack(anchor="center")

conv_titre = Label(conv_main, text="Conversion", font=(16)).grid(row=0, column=0, columnspan=2, pady=10)

lbl_Montant = Label(conv_main, text="Montant :", width=10).grid(row=1, column=0)
montant = Entry(conv_main, width=30)
montant.grid(row=1, column=1)

lbl_Monnaie_init = Label(conv_main, text="De :", width=10).grid(row=2, column=0)
Monnaie1 = OptionMenu(conv_main, monnaie_Depart, *liste_devise)
Monnaie1.config(width=24)
Monnaie1.grid(row=2, column=1)

lbl_Monnaie_conv = Label(conv_main, text="A :", width=10).grid(row=3, column=0)
Monnaie2 = OptionMenu(conv_main, monnaie_Fin, *liste_devise)
Monnaie2.config(width=24)
Monnaie2.grid(row=3, column=1)

btn_convertir = Button(conv_main, text="Convertir", command=Convertir, width= 25).grid(row=4, column=1, padx=10, pady= 10)

lbl_Resultat = Label(conv_main, text="Resultat", width=10).grid(row=5, column=1)
resultat = Entry(conv_main, width=30)
resultat.grid(row=5, column=1)

# Ajout de devises

ajt_devise = Frame(fenetre, pady=10)
ajt_devise.pack(anchor="center")

devise_titre = Label(ajt_devise, text="Ajout de devise", font=(16)).grid(row=0, column=0, columnspan=2, pady=10)

lbl_nom_devise = Label(ajt_devise, text="Nom :", width=10).grid(row=1, column=0)
nom_devise = Entry(ajt_devise, width=30)
nom_devise.grid(row=1, column=1)

lbl_valeur_devise = Label(ajt_devise, text="Taux :", width=10).grid(row=2, column=0)
valeur_devise = Entry(ajt_devise, width=30)
valeur_devise.grid(row=2, column=1)

btn_ajout = Button(ajt_devise, text="Ajouter", command=Ajout_Devise, width= 25).grid(row=3, column=1, padx=10, pady= 10)

# Historique des conversions

conv_hist = Frame(fenetre, pady=10)
conv_hist.pack(anchor="center")

hist_titre = Label(conv_hist, text="Historique", font=(16)).pack(pady=10)
btn_vide_hist = Button(conv_hist, text="Vider l'historique", command= suppr_historique)
btn_vide_hist.pack(fill="both", expand="yes")
hist = Frame(conv_hist)
hist.pack(fill="both", expand="yes")


fenetre.mainloop()