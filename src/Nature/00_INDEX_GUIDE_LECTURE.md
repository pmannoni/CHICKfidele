# 📚 GUIDE COMPLET ANALYSE MÉTHODOLOGIQUE CHIKUNGUNYA
## Publication : "Transmission and Strategy Analysis of Chikungunya" (Foshan 2025)

---

## 🎯 STRUCTURE DES 4 DOCUMENTS

### **Document 1 : CHIKV_Analyse_Methodologie.md** (17 KB)
**Parties 1-13 : FONDATIONS DU MODÈLE**

| Partie | Contenu |
|--------|---------|
| 1 | **Architecture globale** : Structure humains (10k) + moustiques (5) = 35 variables |
| 2 | **Système ODE complet** : Équations humains (sexe/âge) et moustiques (larves+adultes) |
| 3 | **Paramètres biologiques** : Tableau complet 20+ paramètres (fixes et à estimer) |
| 4 | **Nombre reproduction ℛ₀** : Décomposition théorique + Formules explicites |
| 5 | **5 Hypothèses biologiques** : Transmission inter-espèces, structure sexe-âge, saisonnalité |
| 6-7 | **Estimation PMCMC** : Particle Filter + Metropolis-Hastings algorithm |
| 8 | **Analyse Next-Generation Matrix** : Calcul ℛ₀ par DFE |
| 9 | **Phases épidémiologiques Foshan 2025** : Chronologie + Compositions démographiques |
| 10-13 | **Données preprocessing** : Nettoyage, QA masks, normalisations, résolutions |

**👉 À LIRE EN PREMIER pour comprendre structure modèle**

---

### **Document 2 : CHIKV_Analyse_Methodologie_Part2.md** (15 KB)
**Parties 14-22 : SYSTÈME CONTRÔLE OPTIMAL**

| Partie | Contenu |
|--------|---------|
| 14 | **3 Voies intervention** : u₁ (mosquito→humain), u₂ (humain→mosquito), u₃ (suppression) |
| 15 | **Fonction objectif** : Lagrangien = cas symptomatiques + coûts u² |
| 16 | **Théorie Pontryagin** : Construction Hamiltonien + Conditions optimalité + Contrôles explicites |
| 17 | **8 Stratégies évaluées** : Matrice u₁,u₂,u₃ combinations + efficacités (17.8% → 95.8%) |
| 18 | **Heatmaps 3D** : Analyse R_eff en fonction (u₁,u₂,u₃) ∈ [0,1]³ |
| 19 | **Intensités réelles Foshan** : Trajectoires u_i(t) observées et moyennes (70-74%) |
| 20 | **Étapes implicites** : Hypothèses non documentées (linéarité, immédiateté, compliance) |
| 21 | **Ambiguïtés détectées** : Poids p_sj, coûts p_{k+i}, IRR, dates transitions |
| 22 | **Paramètres sensibles** : Identification q, x, a comme très sensibles |

**👉 ESSENTIEL pour comprendre optimisation et ambiguïtés**

---

### **Document 3 : CHIKV_Analyse_Methodologie_Part3.md** (45 KB)
**Parties 23-26 : PIPELINE COMPLET + PSEUDO-CODE + IMPLÉMENTATION**

| Partie | Contenu |
|--------|---------|
| 23 | **Pipeline complet** : 9 étapes (données → résultats) avec diagramme ASCII |
| 24 | **Pseudo-code détaillé** : 3 Algorithmes |
|    | • Algo 1 : PMCMC avec Particle Filter |
|    | • Algo 2 : Forward-Backward Sweep optimal control |
|    | • Algo 3 : 3D parameter sweep R_eff analysis |
| 25 | **Implémentation Python** : 600+ lignes (classes, ODEs, estimation, reproduction) |
| 26 | **Ambiguïtés + paramètres manquants** : Tableau critique issues |

**👉 POUR REPRODUIRE L'ÉTUDE COMPLÈTE**

---

### **Document 4 : CHIKV_Synthese_Ambiguitites.md** (15 KB)
**SYNTHÈSE FINALE : Tous les problèmes identifiés**

| Section | Contenu |
|---------|---------|
| Tableau 1 | Paramètres status (✓ clé / ⚠️ manquant / ❌ MANQUANT) |
| Tableau 2 | 11 étapes implicites/partiellement documentées |
| Tableau 3 | Résolutions spatiales/temporelles/démographiques |
| Tableau 4 | Vérification composantes équations |
| Tableau 5 | Décomposition ℛ₀ (formules + résultats empiriques) |
| Tableau 6 | Comparaison efficacité 8 stratégies |
| Tableau 7 | Sensibilité paramètres (q, a, x très sensibles) |
| **Tableau 8** | **LISTE MANQUEMENTS** : S1 IRR, S2 poids, S3 x₀, S4 chronogramme |
| Tableau 9 | Métriques validation (AIC/BIC/RMSE manquants) |
| Checklist | 9 points avant implémentation |
| Verdict | Solidité 7/10 | Reproductibilité 5/10 | Applicabilité 8/10 |

**👉 POUR IDENTIFIER TOUS LES MANQUEMENTS ET FAIRE REPRODUCTION**

---

## 📊 STRUCTURE LOGIQUE DE LECTURE

### **Scénario 1 : Comprendre la science rapidement (2h)**
```
1. Synthèse_Ambiguitites.md (Tableaux 1-6)
2. Analyse_Methodologie.md (Parties 1-4 : Architecture + ℛ₀)
3. Analyse_Methodologie_Part2.md (Parties 14-17 : Contrôle optimal)
```

### **Scénario 2 : Reproduire l'étude complète (1-2 semaines)**
```
1. Synthèse_Ambiguitites.md (Tableau 8 : Manquements)
2. Analyse_Methodologie.md (Parties 1-13 : ODE system)
3. Analyse_Methodologie_Part2.md (Parties 14-22 : Control)
4. Analyse_Methodologie_Part3.md (Parties 23-25 : Pipeline + Pseudo-code)
5. Coder implémentation Python (utiliser code Part3 comme template)
6. Obtenir Tableau S1 (IRR) auprès auteurs
7. Tester sur données Foshan réelles
```

### **Scénario 3 : Implémenter nouvel article similaire (1-2 semaines)**
```
1. Analyse_Methodologie_Part3.md (Algorithme général + pipeline)
2. Adapter priors + données locales
3. Valider sur publication existante d'abord
4. Appliquer à nouveau système épidémiologique
```

---

## 🔴 AMBIGUÏTÉS CRITIQUES À RÉSOUDRE

| Tier | Problème | Impact | Solution |
|------|----------|--------|----------|
| **1** | **Poids objectif p_sj MANQUANTS** | Impossible allocations ressources exactes | Contacter auteurs pour Tableau S2 |
| **1** | **Tableau S1 IRR non fourni** | Impossible reproduire ℛ₀ exact | Demander IRR_sj complet |
| **1** | **Coûts intervention p_{k+1,2,3} MANQUANTS** | Impossible reproduire u* | Spécifier ou estimer |
| **2** | **Choix k=3 âges non-justifiée** | Résultats dépendent k | Sensitivité k=2,4,5 |
| **2** | **Phase saisonnière τ=30 non-justifiée** | Pic peut être décalé | Justifier vs données T |
| **3** | **Paramètres PMCMC omis** (N_filter, burn_in, priors) | Difficile reproduire postérior | Documenter PMCMC details |

---

## 📐 FORMULES CLÉS (Quick Reference)

### ℛ₀ Décomposition
```
ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))

ℛ₀(vp) = Σ_j,s [ β_vp·IRR_sj·S_sj0 · (pathways I + A) ] / N_p

ℛ₀(pv) = β_pv·S_v0 / N_p · ϖ/(d+ϖ) · 1/d
```

### Contrôles Optimaux
```
u₁*(t) = clamp[ Σ_j [ (η_E - η_S)·β_vp·IRR·S·I_v/N_p ] / p_{k+1} ]
u₂*(t) = clamp[ (η_E_v - η_S_v)·β_pv·S_v·I_tot/N_p / p_{k+2} ]
u₃*(t) = clamp[ η_S_a·a·c(t)·x·N_p / p_{k+3} ]

où clamp(x) = max{u_min, min{u_max, x}}
```

### ODE Core (Humains)
```
dS_sj/dt = -(1-u₁)·β_vp·IRR_sj·S_sj·I_v / N_p
dE_sj/dt = ... - (q·ω' + (1-q)·ω)·E_sj
dI_sj/dt = (1-q)·ω·E_sj - γ·I_sj
dA_sj/dt = q·ω'·E_sj - γ'·A_sj
```

---

## 📊 RÉSULTATS CLÉS (EMPIRIQUES FOSHAN 2025)

| Métrique | Phase Préparation | Phase Confinement | Ratio |
|----------|------------------|-------------------|-------|
| **ℛ₀ global** | 10.1235 | 1.3865 | 7.3× |
| **ℛ₀(vp)** | 3.6197 | 0.8665 | 4.2× |
| **ℛ₀(pv)** | 28.3132 | 2.2185 | 12.8× |
| **Cas cumulés** | ~2,000 (33j) | ~7,900 (61j) | 3.9× |

### Stratégies Efficacité
- **Meilleure seule :** u₃ (suppression mosquito) = 78.5% ✅
- **Meilleur pair :** u₁+u₃ = 81.5% ✅✅
- **Optimal tous trois :** u₁+u₂+u₃ = 95.8% ✅✅✅

### Groupes Vulnérables
- **Plus impactés :** Males 15-59 ans (transmission core group)
- **Moins impactés :** Females 60+ ans (ℛ₀ baseline faible)

---

## 🔧 PARAMÈTRES À SPÉCIFIER AVANT CODE

```python
# DOIVENT ÊTRE SPÉCIFIÉS
params_to_specify = {
    'beta_vp': None,           # ← PMCMC estime
    'beta_pv': None,           # ← PMCMC estime
    'x': None,                 # ← PMCMC estime
    'IRR': {
        'm': {0: ???, 1: ???, 2: ???},  # ← Tableau S1 MANQUANT
        'f': {0: ???, 1: ???, 2: ???}
    },
    'p_m0': ???, 'p_m1': ???, 'p_m2': ???,  # ← Tableau S2 MANQUANT
    'p_f0': ???, 'p_f1': ???, 'p_f2': ???,
    'p_k1': ???, 'p_k2': ???, 'p_k3': ???,
    'u_min': 0.2,              # ✓ Spécifié
    'u_max': 0.8,              # ✓ Spécifié
}

# PMCMC Algorithm 1
pmcmc_settings = {
    'N_particles': ???,        # Assumé 500
    'K_iterations': ???,       # Assumé 5000
    'K_burnin': ???,          # Assumé 1000
    'proposal_sd': ???,       # À calibrer
    'prior_beta_vp': ???,     # MANQUANT
    'prior_beta_pv': ???,     # MANQUANT
    'prior_x': ???,           # MANQUANT
}

# Forward-Backward Sweep Algorithm 2
fbsweep_settings = {
    'n_iterations': ???,      # Assumé 50
    'relaxation_factor': ???, # Assumé 0.5
    'tolerance': 1e-4,        # Assumé
    'dt': 0.01,              # Assumé
}
```

---

## ✅ CHECKLIST AVANT REPRODUCTION

- [ ] **Obtenir Tableau S1** : Tous IRR_sj avec IC 95%
- [ ] **Obtenir/Spécifier Tableau S2** : Poids objectif p_sj, p_k+i
- [ ] **Définir priors PMCMC** : Lognormal? Uniform? Justification?
- [ ] **Fixer conditions initiales** : x₀ jour 1 (nombre E, I, A)
- [ ] **Documenter PMCMC details** : N_filter, K_iter, burn_in exacts
- [ ] **Justifier k=3 âges** : Pourquoi pas k=2,4? Sensitivité?
- [ ] **Justifier τ=30 saisonnnier** : Pourquoi 30 jours phase?
- [ ] **Estimer lags** : Report cases (symptôme→diag→report)
- [ ] **Compliance u_i** : Efficacité réelle des interventions
- [ ] **Sensitivité** : Pareto frontiers, Morris screening, Sobol

---

## 📚 DOCUMENTS EXTERNES REQUIS

Pour **COMPLÈTE** reproductibilité:

1. **Données empiriques**
   - WHO epidemiological data (Jun-Sep 2025)
   - Ministry of Health Foshan confirmed/suspected cases
   - Bureau Statistics Foshan (population age-sex)

2. **Littérature paramètres** (références Document 1, Tableau 4)
   - q, ω, ω', γ, γ' : [34-35] de Cavalcanti & Alade
   - λ, d, a : [24-29] références
   - ϖ, n : [26-33] références transmission verticale

3. **Supplementary Materials (MANQUANTS)**
   - Tableau S1 : IRR détail toutes les combinaisons
   - Tableau S2 : Poids p_sj, p_cost
   - Tableau S3 : Conditions initiales jour 1
   - Tableau S4 : Chronogramme u_i(t) journalier
   - Figure S1 : Goodness-of-fit comparisons

---

## 🎓 APPRENTISSAGE TRANSFÉRABLE

Ce framework s'applique à:
- ✅ Dengue (même vecteur *Aedes*)
- ✅ Zika (même mécanisme transmission)
- ✅ Malaria (modèle structure similar, changement vecteur)
- ✅ COVID-19 (ODE structure similaire, sans composante mosquito)

**Étapes généralisables :**
1. Next-gen matrix calcul ℛ₀ (universel pour transmission chaînes)
2. Pontryagin optimal control (applicable maladies quelconques)
3. PMCMC estimation (robuste pour params epidémio)
4. Heatmap sensitivité (multi-intervention analysis)

---

## 🎯 RÉSUMÉ EXECUTIF (30 SECONDES)

**Qu'est-ce que c'est?**
Modèle SEIAR âge-sexe structuré + contrôle optimal Hamiltonien pour épidémie Chikungunya Foshan 2025.

**Résultat clé?**
Suppression moustiques (u₃) est **78.5%** efficace seule. Combinaison u₁+u₃ = **81.5%**. Tous trois = **95.8%**.

**Problème?**
5 paramètres critiques manquants (IRR, poids objectif, coûts). Reproductibilité = 5/10.

**Solution?**
Contacter auteurs pour Tableaux S1-S4. Ensuite: faisable en 1 semaine avec code Part 3.

---

**Créé:** 25 May 2026  
**Analyse version:** 1.0 Final  
**Statut:** Prêt pour reproduction avec ajustements
