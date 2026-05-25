# SYNTHÈSE FINALE
## Ambiguïtés, Paramètres Manquants et Tableau de Reproduction

---

## RÉSUMÉ EXÉCUTIF

Publication : **"Transmission and strategy analysis of Chikungunya among demographic groups: Proposing an optimal control framework"**

**Modèle :** Système SEIAR structuré par sexe et âge avec dynamique moustique (larves + adultes)
- **Dimension :** 35 variables (10k+5, k=3 groupes âge)
- **Données :** Épidémie Foshan 2025 (16 Jun - 18 Sep)
- **Paramètres à estimer :** β_vp, β_pv, x, IRR_sj (PMCMC)
- **Intervention analyse :** Contrôle optimal (Hamiltonien) pour u₁, u₂, u₃

---

## TABLEAU 1 : PARAMÈTRES CRITIQUES - STATUS

| Paramètre | Valeur/Plage | Source | Status | Implication |
|-----------|--------------|--------|--------|-------------|
| **β_vp** | À estimer | PMCMC (Phase 1) | ⚠️ Clé | Transmission mosquito→humain |
| **β_pv** | À estimer | PMCMC (Phase 1) | ⚠️ Clé | Transmission humain→mosquito |
| **x** (ratio mosquito/H) | 5-15 | PMCMC | ⚠️ Critique | Taille population moustique |
| **IRR_sj** | Voir Tableau S1 | Données empiriques | 📋 Clé | Hétérogénéité transmission |
| **q** | 0.155 | [0.03-0.28] littérature | ✓ Fixe | Probabilité asymptomatique |
| **ω, ω'** | 1/4.5 jour⁻¹ | Littérature | ✓ Fixe | Taux latence humain |
| **γ, γ'** | 1/7 jour⁻¹ | Littérature | ✓ Fixe | Taux guérison |
| **λ** | 0.0902 jour⁻¹ | Littérature | ✓ Fixe | Émergence larvaire |
| **d** | 1/7.4 jour⁻¹ | Littérature | ✓ Fixe | Mortalité moustique |
| **a** | 0.145 jour⁻¹ | [0.02-0.27] littérature | ✓ Fixe | Natalité moustique |
| **ϖ** | 1/5.5 jour⁻¹ | Littérature | ✓ Fixe | Incubation extrinsèque |
| **n** | 0.0181 | [0.0076-0.0286] littérature | ✓ Fixe | Transmission verticale |
| **τ** | 30 jours | Spécifié | ? Non-clair | Phase saisonnière |
| **T** | 365 jours | Spécifié | ✓ Fixe | Période saisonnière |
| **N_p** | 7.3 M (Foshan 2025) | Bureau Statistiques | ✓ Fixe | Population totale |
| **p_sj** | **MANQUANT** | - | ❌ MANQUANT | Poids cas groupe (sj) dans objectif |
| **p_{k+1}** | **MANQUANT** | - | ❌ MANQUANT | Coût u₁ |
| **p_{k+2}** | **MANQUANT** | - | ❌ MANQUANT | Coût u₂ |
| **p_{k+3}** | **MANQUANT** | - | ❌ MANQUANT | Coût u₃ |
| **u_min** | 0.2 | Spécifié | ✓ Raisonnable | Contrôle minimum |
| **u_max** | 0.8 | Spécifié | ✓ Raisonnable | Contrôle maximum |

**Légende :** ✓ Bien défini | ⚠️ Critique/Clé | ❌ MANQUANT | ? Unclear | 📋 Attaché

---

## TABLEAU 2 : ÉTAPES IMPLICITES OU PARTIELLEMENT DOCUMENTÉES

| Étape | Documentation | Détail | Implication |
|-------|---------------|--------|-------------|
| **Calcul IRR** | Implicite | Ratio incidence brut groupe / incidence référence | **Sensibilité inconnue** |
| **Sélection k=3 âges** | Implicite | Pourquoi 0-14, 15-59, 60+ ? | Résultats dépendent de k |
| **Normalisation données** | Implicite | Offset symptôme→diagnostic approx 1-2j | Chronologie +/- 2j ambiguë |
| **Lissage série temps** | Implicite | Filters appliqués? Smooth splines? | Peut biaiser ℛ₀ estimation |
| **Initial conditions** | Implicite | Compartiments jour 0 non spécifiés | Sensibilité x₀ non testée |
| **Estimation IRR temporelle** | Implicite | Fixed vs variant par phase? | IRR_phase1 ≠ IRR_phase2 ? |
| **Délai report cas** | Implicite | Diagnostiqué jour t vs rapporté jour t+Δt | Shift chronologique non modélisé |
| **Ajustement poids objective** | Implicite | Comment p_sj, p_{k+i} calibrés? | Post-hoc pour matching trajectoires obs? |
| **Allocation poids by sexe** | Implicite | p_m vs p_f : même poids? | Asymétrie possible |
| **Compliance réelle u_i** | Implicite | u₃ observé = efficacité réelle spray? | Facteur réduction non-linéaire? |
| **Retards implémentation** | Implicite | Contrôle implémenté jour même? | Lag 1-3 jours omis |

---

## TABLEAU 3 : RÉSOLUTIONS SPATIALES & TEMPORELLES

| Dimension | Résolution | Status | Justification | Impact |
|-----------|-----------|--------|---------------|--------|
| **Spatial** | 0D (Foshan globalement) | ✓ Spécifié | Homogeneous mixing | Pas de spillover inter-districts |
| **Temporelle ODE** | Δt = 0.01 jour (RK4) | ✓ Implicite | Stabilité numérique | Bon |
| **Temporelle data** | Journalière (cases/jour) | ✓ Spécifié | Observation 16 Jun - 18 Sep | Fin observation arbitraire |
| **Démographique** | 6 groupes (2 sexe × 3 âge) | ⚠️ Clé | k=3 non justifié | Sens. k=2,4,5 non testée |
| **Saisonnier** | Annuel (cos cycle) | ✓ Spécifié | τ=30, T=365 | Phase τ=30 non-justifiée |

---

## TABLEAU 4 : COMPOSANTES ÉQUATIONS CLÉS (VÉRIFICATION)

| Équation | Status | Notes |
|----------|--------|-------|
| **dS_sj/dt = -(1-u₁)·β_vp·IRR_sj·S_sj·I_v / N_p** | ✓ Spécifiée | Force infection mosquito→humain |
| **dE_sj/dt** | ✓ Spécifiée | Branchement q → (A vs I) |
| **dI_sj/dt, dA_sj/dt** | ✓ Spécifiée | Symptomatiques vs asymptomatiques |
| **dR_sj/dt** | ✓ Spécifiée | Guérison simple (pas réinfection) |
| **dS_a/dt = a·c(t)·((1-u₃)·x·N_p - n·I_a) - λ·S_a** | ✓ Spécifiée | Natalité saisonnière |
| **dI_a/dt = a·c(t)·n·I_a - λ·I_a** | ✓ Spécifiée | Transmission verticale |
| **dS_v/dt** | ✓ Spécifiée | Émergence larves + infection |
| **dE_v/dt** | ✓ Spécifiée | Incubation extrinsèque (EIP) |
| **dI_v/dt** | ✓ Spécifiée | Infectiosité adulte |

---

## TABLEAU 5 : DÉCOMPOSITION ℛ₀ - FORMULES & RÉSULTATS

### A. Formules Décomposition

```
ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))

ℛ₀(vp) = Σ_j,s [ I_pathway_sj + A_pathway_sj ]

où :
  I_pathway_sj = β_vp·IRR_sj·S_sj0 · (1-q)·ω / [γ·(q·ω'+(1-q)·ω)] / N_p
  A_pathway_sj = β_vp·IRR_sj·S_sj0 · q·ω' / [γ'·(q·ω'+(1-q)·ω)] / N_p

ℛ₀(pv) = β_pv·S_v0 / N_p · ϖ/(d+ϖ) · 1/d
```

### B. Résultats Empiriques Foshan 2025

| Période | ℛ₀ Total | ℛ₀(vp) | ℛ₀(pv) | Status | Interprétation |
|---------|----------|--------|--------|--------|-----------------|
| 11 Jun-18 Jul | **10.1235** | 3.6197 | 28.3132 | 📊 Observé | **Très explosif** |
| 19 Jul-18 Sep | **1.3865** | 0.8665 | 2.2185 | 📊 Observé | **Contrôlé** |
| 19 Jul-25 Jul | **1.2934** | 1.0341 | 1.6178 | 📊 Observé | Transition |
| 26 Jul-18 Sep | **1.3243** | 0.8122 | 2.1593 | 📊 Observé | Persistance |

**Observations clés :**
- Phase préparation : **ℛ₀(pv) >> ℛ₀(vp)** (28 vs 3.6)
  - Explication : Transmission humain→mosquito FORTEMENT dominante
  - Implication : Bloquer H→V (u₂) très efficace
  
- Phase confinement : Rapport se rééquilibre mais ℛ₀ << 1 (équivalent)
  - ℛ₀(pv) décline moins = mosquitos persistants
  - ℛ₀(vp) décline plus = u₁ effectif

---

## TABLEAU 6 : STRATÉGIES CONTRÔLE - COMPARAISON EFFICACITÉ

| # | Stratégie | u₁ | u₂ | u₃ | % Réduction | Meilleur Pour | Limitation |
|----|-----------|----|----|-----|-----------|---------------|----------|
| **1** | Aucun contrôle | 0 | 0 | 0 | 0% (baseline) | - | Épidémie incontrôlée |
| **2** | u₁ seul | HMC | 0 | 0 | 17.8% | Females 0-14 | Très faible |
| **3** | u₂ seul | 0 | HMC | 0 | 25.6% | Males 15-59 | Faible |
| **4** | u₃ seul | 0 | 0 | HMC | **78.5%** ⭐ | Tous groupes | ✓ Meilleur seul |
| **5** | u₁+u₂ | HMC | HMC | 0 | 35.8% | Females 0-14 | Bloquer late en cascade |
| **6** | u₁+u₃ | HMC | 0 | HMC | **81.5%** ⭐⭐ | Males 15-59 | ✓ Meilleur pair |
| **7** | u₂+u₃ | 0 | HMC | HMC | 80.7% | Tous groupes | Légèrement < u₁+u₃ |
| **8** | u₁+u₂+u₃ | HMC | HMC | HMC | **95.8%** ⭐⭐⭐ | Tous groupes | ✓ Optimal |

**Hiérarchie efficacité :** u₃ > u₂ > u₁ (confirmé)

---

## TABLEAU 7 : PARAMÈTRES SENSIBLES - PLAGES VARIABILITÉ

| Paramètre | Valeur nominale | Plage doc. | Facteur | Sensitivité ℛ₀ |
|-----------|-----------------|-----------|---------|-----------------|
| **q** | 0.155 | 0.03-0.28 | 9.3× | **TRÈS HAUTE** |
| **a** | 0.145 | 0.02-0.27 | 13.5× | **TRÈS HAUTE** |
| **x** | 10 | 5-15 | 3× | **HAUTE** |
| **ω, ω'** | 1/4.5 | 1/7 to 0.5 | 2.8× | Modéré |
| **d** | 1/7.4 | 1/9.8 to 1/4.5 | 2.2× | Modéré |
| **ϖ** | 1/5.5 | 1/8.2 to 1/3 | 2.7× | Modéré |

**⚠️ Action requise :** Analyse de sensibilité globale (Sobol, Morris) pour q et a

---

## AMBIGUÏTÉS DÉTECTÉES (TIER 1 = CRITIQUE)

### Tier 1 - Critiques (Bloquant pour reproductibilité)

| # | Ambiguïté | Conséquence | Solution |
|----|-----------|-----------|----------|
| **A1** | **Poids objectif p_sj non spécifiés** | Allocations ressources ambiguës | Publier Tableau S pour tous p_sj |
| **A2** | **Coûts d'intervention p_{k+1,2,3} manquants** | Impossible reproduire u* exact | Spécifier coûts $/jour |
| **A3** | **Tableau S1 (IRR détail) non fourni** | Impossible reproduire ℛ₀ exact | Tableau S1 in supplementary |
| **A4** | **Dates transitions u_i non détaillées** | Reconstruction chronologie imprécise | Chronogramme journalier |
| **A5** | **Poids par sexe dans objectif (p_m vs p_f)** | Asymétrie décision non-claire | Spécifier ou justifier égalité |

### Tier 2 - Modérés (Affectent validité mais pas bloqu)

| # | Ambiguïté | Conséquence | Action |
|----|-----------|-----------|--------|
| **A6** | **Choix k=3 âges non justifié** | Résultats dépendent k | Sensitivité k=2,4,5 |
| **A7** | **Phase saisonnière τ=30 non-justifiée** | Pic prédictions peut être décalé | Justifier vs données T |
| **A8** | **IRR constants vs variant par phase** | ℛ₀ estimation biais si IRR change | Analyser IRR_phase1 vs phase2 |
| **A9** | **Retards report cas omis** | Lag 1-2 jours ignoré | Estimer lag, sensitivité |
| **A10** | **Compliance réelle u_i non quantifiée** | u_observé ≠ u_effectif | Études post-hoc compliance |

### Tier 3 - Mineurs (Documentés mais non complètement)

| # | Ambiguïté | Mitigation |
|----|-----------|-----------|
| **A11** | **Conditions initiales (jour 1) imprécises** | x₀ sensitivité analysée ✓ |
| **A12** | **Délai implémentation contrôle assumé ≈0** | Impact petit (<1j) mais mentionner |
| **A13** | **Pas de vaccination modélisée** | Documente comme limitation ✓ |

---

## TABLEAU 8 : LISTE COMPLÈTE PARAMÈTRES À FOURNIR

### Avant soumission document:

```
Tableau Manquant S1 (OBLIGATOIRE):
  IRR_sj pour tous s ∈ {m,f}, j ∈ {0,1,2}
  ├─ Calcul: Incidence_sj / Incidence_reference
  └─ Intervalles de confiance 95%

Tableau Manquant S2 (Optionnel mais utile):
  Poids objectif:
  ├─ p_mj, p_fj pour j=0,1,2
  ├─ p_{k+1}, p_{k+2}, p_{k+3}
  └─ Justification ou calibration procedure

Tableau Manquant S3 (Optionnel):
  Conditions initiales x₀:
  ├─ S_sj(0), E_sj(0), I_sj(0) par groupe
  └─ Source: données jour 16 Jun ou équilibre

Chronogramme Manquant S4 (Pratique):
  Trajectoires u_i(t) observées:
  ├─ Jour, u₁, u₂, u₃ (journalière)
  └─ Ou spline smooth coefficients
```

---

## ÉTAPES IMPLICITES REQUÉRANT CLARIFICATION

### Flux de travail PMCMC (Algorithme 1)

**Question 1 :** Nombre de particules N_filter?
- Document muet → Assumé N ≈ 500 (standard)
- **À confirmer**

**Question 2 :** Nombre itérations MCMC burn-in?
- Document muet → Assumé K_iter ≈ 5000, burn ≈ 1000
- **À confirmer**

**Question 3 :** Priors sur β_vp, β_pv, x?
- Document muet → Assumé uniform ou lognormal
- **CRITICAL** pour résultats posterior

### Forward-Backward Sweep (Algorithme 2)

**Question 4 :** Facteur d'amortissement ω?
- Document muet → Assumé ω = 0.5
- **À confirmer**

**Question 5 :** Nombre d'itérations forward-backward?
- Document muet → Assumé ~50 iterations
- **À confirmer**

**Question 6 :** Critère convergence ||u^(k) - u^(k-1)||?
- Document muet → Assumé ε = 10⁻⁴
- **À confirmer**

### Paramétrisation Phase Saisonnière

**Question 7 :** τ=30 jours = quelle justification ?
- Phase "décalée 30 jours du 1 janvier" ?
- Correspond à "pic début février" (été Chine du sud)?
- **Clarifier ou reference**

---

## TABLEAU 9 : VALIDATION MODÈLE (GOODNESS-OF-FIT)

### Métriques Rapportées

| Métrique | Valeur | Status | Notes |
|----------|--------|--------|-------|
| **Comparaison Fig 3** | Courbes générales match | ✓ Visual | Match qualitative acceptable |
| **Décomposition ℛ₀** | Contributions par groupe | ✓ Rapporté | Asymptos > symptos (attendu) |
| **AIC/BIC** | Non rapporté | ❌ MANQUANT | Comparaison k=2,3,4 absent |
| **RMSE by group** | Non rapporté | ❌ MANQUANT | Erreurs détaillées par groupe |
| **Cross-validation** | Non discutée | ❌ MANQUANT | Généralisation non testée |

---

## CHECKLIS REPRODUCTION (AVANT IMPLÉMENTATION)

- [ ] **Obtenir Tableau S1 (IRR)** - Contact authors si nécessaire
- [ ] **Spécifier priors PMCMC** - Lognormal sur β_vp, β_pv? Uniform sur x?
- [ ] **Fixer poids objectif** - p_sj = 1 (uniform)? p_{k+i} = 1 (equal cost)?
- [ ] **Conditions initiales** - jour 1 : combien de E, I, A par groupe?
- [ ] **Paramètres numériques** - N_filter, K_iter, burn_in, ω, ε
- [ ] **Délai report** - lag symptôme→diagnostic quantifié
- [ ] **Sensitivité k** - Réexécuter avec k=2,4 pour tester
- [ ] **Phase saisonnière** - Justifier τ=30 vs τ=0 vs fit data
- [ ] **Tests unitaires ODE** - Vérifier dérivées analytiques vs RK4

---

## SYNTHÈSE FINALE

### Solidité Méthodologie : **7/10**

**Points forts :**
✅ Modèle structuré (sexe-âge) approprié
✅ Framework contrôle optimal rigoureux (Pontryagin)
✅ Données qualité élevée (Foshan 2025)
✅ Analyse décomposition ℛ₀ insightful
✅ Validation stratégies alternatives systématique

**Points faibles :**
❌ Paramètres clés manquants (p_sj, p_cost)
❌ Ambiguïtés dans estimations IRR
❌ Choices (k=3 âge, τ=30) non-justifiées
❌ PMCMC details omis
❌ Sensitivité paramètres incomplète

### Reproductibilité : **5/10**

Avec Tableau S1,S2,S3 fourni → 8/10
Actuellement : 5/10 (manquent trop détails numériques)

### Applicabilité : **8/10**

Framework adaptable à autres épidémies vecteurs
Mais nécessite data locale (IRR, population) de qualité

---

**Conclusion :** Publication scientifiquement solide mais **nécessite matériel supplémentaire** pour reproductibilité complète. Auteurs devraient publier tous Tableaux S (IRR, poids, conditions initiales) en annexe.

