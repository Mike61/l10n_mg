# Madagascar - Comptabilité et Fiscalité

Ce module est la base de la Comptabilité à Madagascar.
Comptatible avec odoo v9.
Calqué sur les publications du PCG 2005 et la feuille de déclaration de TVA.

Le plan de compte et des Positions fiscales:

* **nationaux assujetis** : des agents économiques nationaux qui doivent déclarer leurs TVA (déductibles et collectés)
* **nationaux non assujetis** : des agents économiques nationaux qui ne déclarent pas leurs TVA
* **nationaux non assujetis** : des agents économiques nationaux mais non taxés (pas de TVA dans leurs factures)
* **reste du monde** : des agents économiques étrangers, qui ne payent pas la TVA

Les taxes détaillées selon la loi des finances.

ATTENTION : la modification pour models/chart_template permet de configurer avant l'activation du module l10n_mg le nombre de digit

#Usage

* activer l'application Finances et Comptabilité
* configurer le Nb de digits dans la fiche de la société
* activer le module l10n_mg

#Known issues / Roadmap


 * TODO: validation par des spécialistes en comptabilité et finances et droits fiscaux Malagasy
 * TODO: revue des textes, titres, libellés, mots par des experts
 * TODO: rajouter des options propres à Madagascar dans le wizard de configuration si nécessaire

#Credits

* Equipe Informatique du Groupe Vidzar
* Nos anciens stagiaires de l'ENI

##Contributors

* Harison Frédéric RAMANDANIARIVO <fredericramanda@gmail.com>

##Maintainer

* Harison Frédéric RAMANDANIARIVO <fredericramanda@gmail.com>
* Vous etes tous invités à soumettre des suggestions et des améliorations.
