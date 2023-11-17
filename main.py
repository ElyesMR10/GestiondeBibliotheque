
import tkinter as tk
from tkinter import ttk

class FenetreAjoutLivre(tk.Toplevel):
    def __init__(self, parent, ajouter_callback):
        super().__init__(parent)
        self.title("Ajouter un Livre")

        # Étiquettes et saisies pour les détails du livre
        lbl_titre = ttk.Label(self, text="Titre :")
        lbl_titre.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_titre = ttk.Entry(self, font=('Helvetica', 12))
        self.entry_titre.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        lbl_auteur = ttk.Label(self, text="Auteur :")
        lbl_auteur.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_auteur = ttk.Entry(self, font=('Helvetica', 12))
        self.entry_auteur.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Bouton pour ajouter le livre
        btn_ajouter = ttk.Button(self, text="Ajouter", command=self.ajouter_livre)
        btn_ajouter.grid(row=2, columnspan=2, pady=10)

        self.ajouter_callback = ajouter_callback

    def ajouter_livre(self):
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        if titre and auteur:
            self.ajouter_callback(titre, auteur)
            self.destroy()

class ApplicationBibliotheque(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de Bibliothèque")
        self.geometry("400x300")  # Taille de la fenêtre

        # Style pour les éléments ttk
        style = ttk.Style()
        style.configure('TButton', padding=6, relief="flat", background="#ccc")
        style.configure('TLabel', padding=6, font=('Helvetica', 12), background="#eee")

        # Liste des livres (Listbox)
        self.liste_livres = tk.Listbox(self, selectmode=tk.SINGLE, font=('Helvetica', 12))
        self.liste_livres.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Ajout de livres de test
        livres_test = ["Harry Potter", "Lupin", "Les Misérables"]
        for livre in livres_test:
            self.liste_livres.insert(tk.END, livre)

        # Boutons
        self.btn_ajouter_livre = ttk.Button(self, text="Ajouter Livre", command=self.ouvrir_fenetre_ajout_livre)
        self.btn_ajouter_livre.pack(pady=10)

        self.btn_supprimer_livre = ttk.Button(self, text="Supprimer Livre", command=self.supprimer_livre)
        self.btn_supprimer_livre.pack(pady=10)
        
    def ouvrir_fenetre_ajout_livre(self):
        fenetre_ajout = FenetreAjoutLivre(self, self.ajouter_livre)

    def ajouter_livre(self, titre, auteur):
        # Ajouter le livre à la liste des livres dans la fenêtre principale
        livre = f"{titre} - {auteur}"
        self.liste_livres.insert(tk.END, livre)

    def supprimer_livre(self):
        # Supprimer le livre sélectionné de la liste
        selected_index = self.liste_livres.curselection()
        if selected_index:
            self.liste_livres.delete(selected_index)

if __name__ == "__main__":
    app = ApplicationBibliotheque()
    app.mainloop()
