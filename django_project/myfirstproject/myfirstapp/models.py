from django.db import models

class PointDeVente(models.Model):
    code = models.CharField(max_length=255)
    wilaya = models.CharField(max_length=255)
    moughataa = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    gps_lat = models.FloatField()
    gps_long = models.FloatField()

    def __str__(self):
        return self.code 

class FamilleProduit(models.Model):
    label = models.TextField()

    def __str__(self):
        return self.label

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField()
    price_unit = models.TextField()
    code = models.TextField()
    famille_produit_ID = models.ForeignKey(FamilleProduit, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class Price(models.Model):
    value = models.FloatField()
    date = models.DateField()
    point_ID = models.ForeignKey(PointDeVente, on_delete=models.CASCADE)
    produit_ID = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produit_ID.label} - {self.value} - {self.date}"

class Panier(models.Model):
    label = models.TextField()
    code = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.label



class PanierProduit(models.Model):
    price_ID = models.ForeignKey(Price, on_delete=models.CASCADE)
    panier_ID = models.ForeignKey(Panier, on_delete=models.CASCADE)
    ponderation = models.FloatField()

    def __str__(self):
        return f"{self.price_ID.label} - {self.panier_ID.label} - {self.ponderation}"



class INPC(models.Model):
    mois = models.CharField(max_length=20)
    annee_2016 = models.FloatField()
    annee_2017 = models.FloatField()
    annee_2018 = models.FloatField()
    annee_2019 = models.FloatField()
    annee_2020 = models.FloatField()
    annee_2021 = models.FloatField()
    annee_2022 = models.FloatField()
    annee_2023 = models.FloatField()

    def __str__(self):
        return self.mois
