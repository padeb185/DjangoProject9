from django.db import models

class Faculte(models.Model):
    nom = models.CharField(max_length=30)
    couleur = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_de_naissance = models.DateField()
    matricule = models.CharField(max_length=10, unique=True)
    courriel = models.EmailField(unique=True)
    tel_fixe = models.CharField(max_length=20, blank=True, null=True)
    tel_mobile = models.CharField(max_length=20, blank=True, null=True)
    amis = models.ManyToManyField("self", blank=True, symmetrical=True)
    mot_de_passe = models.CharField(max_length=32)
    faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE, related_name="personnes")

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Campus(models.Model):
    nom = models.CharField(max_length=30)
    adresse_postale = models.CharField(max_length=60)

    def __str__(self):
        return self.nom

class Fonction(models.Model):
    intitule = models.CharField(max_length=30)

    def __str__(self):
        return self.intitule

class Employe(Personne):
    bureau = models.CharField(max_length=30)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name="employes")
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE, related_name="employes")

class Cursus(models.Model):
    intitule = models.CharField(max_length=30)

    def __str__(self):
        return self.intitule

class Etudiant(Personne):
    cursus = models.ForeignKey(Cursus, on_delete=models.CASCADE, related_name="etudiants")
    annee = models.IntegerField()

class Message(models.Model):
    auteur = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="messages")
    contenu = models.TextField()
    date_de_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.contenu[:20] + "..." if len(self.contenu) > 20 else self.contenu
