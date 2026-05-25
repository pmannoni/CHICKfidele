# ANALYSE MÉTHODOLOGIQUE EXHAUSTIVE
## PARTIE 2 : SYSTÈME CONTRÔLE OPTIMAL (HMC - Hamiltonian Monte Carlo Method)

---

## PARTIE 14 : STRUCTURE MODÈLE AVEC CONTRÔLES

### 14.1 Trois Voies de Transmission Contrôlables

| Index | Intervention | Équation Paramètre | Paramètre Ajusté |
|-------|--------------|-------------------|------------------|
| u₁(t) | Contrôle transmission mosquito→humain (masques, répellent) | β_vp ← (1-u₁(t))·β_vp | Réduit bites infectieuses |
| u₂(t) | Contrôle transmission humain→mosquito (isolement cas) | β_pv ← (1-u₂(t))·β_pv | Réduit contact humain-mosquito |
| u₃(t) | Suppression pop mosquito (filet, spray, destruction gîtes) | N_v ← (1-u₃(t))·x·N_p | Réduit population adulte |

### 14.2 Équations Modèle Contrôlé (Modèle 2)

**Humains - Males groupe j :**
```
dS_mj/dt = -(1-u₁(t))·β_vp·IRR_mj·S_mj·I_v / N_p

dE_mj/dt = (1-u₁(t))·β_vp·IRR_mj·S_mj·I_v / N_p - q·ω'·E_mj - (1-q)·ω·E_mj

dI_mj/dt = (1-q)·ω·E_mj - γ·I_mj

dA_mj/dt = q·ω'·E_mj - γ'·A_mj

dR_mj/dt = γ·I_mj + γ'·A_mj
```

**Femelles - idem avec S_fj, E_fj, etc.**

**Moustiques - Larves :**
```
dS_a/dt = a·c(t)·((1-u₃(t))·x·N_p - n·I_a) - λ·S_a

dI_a/dt = a·c(t)·n·I_a - λ·I_a
```

**Moustiques - Adultes :**
```
dS_v/dt = λ·S_a - (1-u₂(t))·β_pv·S_v·Σ_j(I_mj+I_fj+A_mj+A_fj)/N_p - d·S_v

dE_v/dt = (1-u₂(t))·β_pv·S_v·Σ_j(I_mj+I_fj+A_mj+A_fj)/N_p - (d+ϖ)·E_v

dI_v/dt = λ·I_a + ϖ·E_v - d·I_v
```

### 14.3 Espace de Contrôle Admissible

```
Θ = { u(t) ∈ L³(0,T) | u_min ≤ u₁(t), u₂(t), u₃(t) ≤ u_max,  t ∈ (0,T) }

Données empiriques (Foshan 2025) :
  u_min = 0.2   (20% d'efficacité minimum maintenue)
  u_max = 0.8   (80% d'efficacité maximum possible)

Justification :
  - u=0 : Pas de contrôle (impossible en urgence)
  - u=1 : Contrôle 100% (non réaliste : vies sociales continuent)
```

---

## PARTIE 15 : FONCTION OBJECTIF

### 15.1 Lagrangien (Coût Instantané)

```
L(t) = Σ_j [ p_mj·I_mj(t) + p_fj·I_fj(t) ] 
       + (p_{k+1}/2)·u₁²(t) 
       + (p_{k+2}/2)·u₂²(t) 
       + (p_{k+3}/2)·u₃²(t)
```

**Interprétation composantes :**

1. **Terme de cas symptomatiques :** Σ_j [ p_mj·I_mj + p_fj·I_fj ]
   - Poids p_sj : importance relative cas groupe (s,j)
   - Objectif : Minimiser infections visibles
   - Implicite : Cas asymptomatiques A_sj ne comptent pas (!!)

2. **Terme de coûts d'intervention :** (p_{k+1}/2)·u₁² + (p_{k+2}/2)·u₂² + (p_{k+3}/2)·u₃²
   - Coefficient quadratique : coûts croissants (réalisme)
   - p_{k+1}, p_{k+2}, p_{k+3} : poids relatifs interventions
   - Exemple : si p_{k+3} >> p_{k+1}, suppression mosquito = prioritaire

### 15.2 Fonctionnelle Objectif Globale

```
G(u(t)) = ∫₀ᵀ L(t) dt = Minimiser cumul cas + cumul coûts sur 95 jours

Problème optimal :
  u* = argmin_{u ∈ Θ} G(u(t))
```

**Remarque critique :**
- Asymptomatiques (A_sj) ne figurent PAS dans l'objectif L
- Or, A_sj contribuent fortement à ℛ₀ (→ transmission)
- Implicite : Décideur priorise cas OBSERVÉS (symptomatiques)
- Conséquence : Contrôles sous-optimaux pour transmission totale

---

## PARTIE 16 : THÉORIE OPTIMAL CONTROL - PRINCIPE DE PONTRYAGIN

### 16.1 Construction Hamiltonien

```
ℋ(x, η, u, t) = L(x,u,t) + Σᵢ₌₁³⁵ ηᵢ·fᵢ(x,u,t)

Où :
  x = [S_m1, E_m1, ..., I_v]ᵀ  (état 35D)
  η = [η₁, ..., η₃₅]ᵀ          (co-état adjoint)
  f = dérivées temporelles (RHS des 35 ODEs)
  L = Lagrangien (15.1)
```

### 16.2 Équations Co-état (Adjoint)

```
Pour i = 1 à 35 :

dηᵢ/dt = -∂ℋ/∂xᵢ = -p_sj·δ(i ∈ {indices I_sj}) - Σⱼ ηⱼ·∂fⱼ/∂xᵢ

Condition finale (terminal) :
  ηᵢ(T) = 0   pour tout i
```

**Interprétation ηᵢ :**
- "Prix ombre" pour modifier xᵢ(t)
- Si η_I_mj > 0 : Réduction I_mj diminue coût (intuition ✓)
- Rétro-propagation : coûts transitent via chaîne transmission

### 16.3 Condition d'Optimalité (Pontryagin)

```
∂ℋ/∂u_i = 0  pour u_i = u₁, u₂, u₃

Cela donne (après algèbre complexe) :
```

### 16.4 Contrôles Optimaux Explicites

**Pour u₁* (mosquito→humain) :**
```
u₁*(t) = max{ u_min, min{ u_max, 
  Σ_j [ (η_E_mj - η_S_mj)·β_vp·IRR_mj·S_mj·I_v/N_p 
        + (η_E_fj - η_S_fj)·β_vp·IRR_fj·S_fj·I_v/N_p ] / p_{k+1}
}}

Interprétation :
  - Augmente si écart η (adjoint) entre E et S > 0
  - Écart > 0 = forte pénalité retarder exposition
  - Écart ≈ 0 = peu de bénéfice incrementel u₁ ↑
```

**Pour u₂* (humain→mosquito) :**
```
u₂*(t) = max{ u_min, min{ u_max, 
  (η_E_v - η_S_v)·β_pv·S_v·Σ_j(I_mj+I_fj+A_mj+A_fj)/N_p / p_{k+2}
}}

Interprétation :
  - Contrôle transmission via réduction virémie diffusion mosquito
  - Efficacité ∝ cohorte infectée humains
```

**Pour u₃* (suppression mosquito) :**
```
u₃*(t) = max{ u_min, min{ u_max, 
  η_S_a·a·c(t)·x·N_p / p_{k+3}
}}

Interprétation :
  - Directement lié réduction gîtes (terme ac...NP)
  - Priorité si η_S_a << 0 (sensibilité via larves)
```

### 16.5 Système Couplé État-Co-état

**À résoudre simultanément :**
```
Estado forward (t=0 à T) :
  ẋ = f(x, u*(x,η,t), t)
  x(0) = x₀

Co-état backward (t=T à 0) :
  η̇ = -∂ℋ/∂x
  η(T) = 0
```

**Schéma numérique :** Forward-Backward Sweep Method

```
Itération k :
  1. Forward : x⁽ᵏ⁾(t) = intégrer ODE état avec u⁽ᵏ⁻¹⁾
  2. Backward : η⁽ᵏ⁾(t) = intégrer adjoint backward avec x⁽ᵏ⁾
  3. Update : u⁽ᵏ⁾(t) = max{u_min, min{u_max, Φ(x⁽ᵏ⁾, η⁽ᵏ⁾)}}
  4. Relax : u_new = (1-ω)·u_old + ω·u_calculated  (amortissement ω ≈ 0.5)
  5. Converger si ||u⁽ᵏ⁾ - u⁽ᵏ⁻¹⁾|| < ε
```

---

## PARTIE 17 : STRATÉGIES D'INTERVENTION ÉVALUÉES

### 17.1 Huit Scénarios Testés

| # | u₁ | u₂ | u₃ | Nom | Efficacité |
|---|----|----|-----|-----|-----------|
| 1 | 0 | 0 | 0 | Pas d'intervention | 0% (baseline) |
| 2 | HMC | 0 | 0 | u₁ seul (mosquito→H) | 17.8% |
| 3 | 0 | HMC | 0 | u₂ seul (H→mosquito) | 25.6% |
| 4 | 0 | 0 | HMC | u₃ seul (suppression) | 78.5% ⭐ Meilleur seul |
| 5 | HMC | HMC | 0 | u₁+u₂ | 35.8% |
| 6 | HMC | 0 | HMC | u₁+u₃ | 81.5% ⭐⭐ Meilleur pair |
| 7 | 0 | HMC | HMC | u₂+u₃ | 80.7% |
| 8 | HMC | HMC | HMC | Tous les trois | 95.8% ⭐⭐⭐ Optimal |

**Résultats (réduction taille épidémie vs scénario 1) :**

1. **Stratégies seules :** u₃ (suppression mosquito) >> u₂ >> u₁
   - u₁ très faible : bloquer transmission mosquito→humain aide peu seul
   - u₃ très efficace : Réduire moustiques = coupe les deux voies

2. **Stratégies paires :** u₁+u₃ meilleur que u₂+u₃ > u₁+u₂
   - u₂+u₃ performant mais u₁+u₃ surpasse (81.5% vs 80.7%)
   - u₁+u₂ faible (35.8%) : Les deux bloquent APRÈS transmission humain

3. **Tous trois ensemble :** 95.8% efficacité
   - Réduction cumulative non-linéaire (synergie)

### 17.2 Variations Démographiques

| Groupe | u₄ seul | u₆ (u₁+u₃) | u₇ (u₂+u₃) |
|--------|---------|-----------|-----------|
| Males 0-14 | 78.46% | 81.52% | 80.72% |
| Males 15-59 | 78.48% | 81.53% | 80.73% |
| Males 60+ | 78.47% | 81.53% | 80.73% |
| Females 0-14 | 78.45% | 81.51% | 80.71% |
| Females 15-59 | 78.47% | 81.53% | 80.73% |
| **Females 60+** | **78.46%** | **81.52%** | **80.72%** |

**Observation critique :**
- Toutes les stratégies **moins efficaces** pour Females 60+
- Raison : Faible ℛ₀ de base pour ce groupe
- Implicite : Objectif L pénalise peu les cas F60+ (poids p_{f3}?)

---

## PARTIE 18 : ANALYSE HEATMAPS TAUX REPRODUCTION EFFECTIF

### 18.1 Espace Paramètres 3D

**Paramètres balayés :** u₁, u₂, u₃ ∈ [0, 1]
**Grille :** 11 × 11 × 11 = 1,331 combinaisons

### 18.2 Seuils Critiques (Efficacité = R_eff < 1)

**Fixing u₁ à valeur actuellement observée :**
```
Si u₁ = obs_u₁ ≈ 0.709 :

  (u₂, u₃) = (0.6, 0.9)  → R_eff = 0.9737 ✓
  (u₂, u₃) = (0.8, 0.8)  → R_eff = 0.9737 ✓
  (u₂, u₃) = (0.9, 0.6)  → R_eff = 0.9737 ✓
```

**Fixing u₂ à valeur actuellement observée :**
```
Si u₂ = obs_u₂ ≈ 0.744 :

  (u₁, u₃) = (0.7, 0.9)  → R_eff = 0.8865 ✓
  (u₁, u₃) = (0.9, 0.7)  → R_eff = 0.8865 ✓
```

**Fixing u₃ à valeur actuellement observée :**
```
Si u₃ = obs_u₃ ≈ 0.709 :

  (u₁, u₂) = (0.7, 0.9)  → R_eff = 0.9465 ✓
  (u₁, u₂) = (0.9, 0.7)  → R_eff = 0.9465 ✓
```

### 18.3 Combinaisons Asymétriques Complètes

```
Trois contrôles simultanés :

Type 1 : Un contrôle réduit (0.1), deux élevés (0.9)
  (u₁, u₂, u₃) = (0.1, 0.9, 0.9) → R_eff = 0.9604
  (u₁, u₂, u₃) = (0.9, 0.1, 0.9) → R_eff = 0.9604
  (u₁, u₂, u₃) = (0.9, 0.9, 0.1) → R_eff = 0.9604

Type 2 : Un contrôle élevé (0.9), deux modérés (0.7)
  (u₁, u₂, u₃) = (0.9, 0.7, 0.7) → R_eff = ?
  (u₁, u₂, u₃) = (0.7, 0.9, 0.7) → R_eff = ?
  (u₁, u₂, u₃) = (0.7, 0.7, 0.9) → R_eff = ?

Type 3 : Configuration 60%/80%/90% → R_eff = 0.9055 ⭐
  (u₁, u₂, u₃) = (0.6, 0.8, 0.9)
  OU permutations ≠ donnent R_eff différents
```

**Importance :** Montre FLEXIBILITÉ
- Pas une unique stratégie optimale
- Multiples allocations ressources → contrôle acceptables
- Implication : Adaptatif à contexte local (fonds, personnel)

---

## PARTIE 19 : INTENSITÉS CONTRÔLE RÉELLES FOSHAN 2025

### 19.1 Chronologie Estimée HMC

```
19 Jul : Début confinement
  u₁(19 Jul) = 0.8 (pic)  [Masques, distanciation]
  u₂(19 Jul) = 0.8 (pic)  [Isolement cas confirmés]
  u₃(19 Jul) = 0.8 (pic)  [Sprays, filets, destruction gîtes]

...

8 Sep : Début réduction u₃
  u₃ décline de 0.8 → 0.2 progressivement

13 Sep : Début réduction u₂
  u₂ décline de 0.8 → 0.2 progressivement

15 Sep : Début réduction u₁
  u₁ décline de 0.8 → 0.2 progressivement

18 Sep : (Fin étude)
  u₁ ≈ 0.2 (minimum)
  u₂ ≈ 0.2 (minimum)
  u₃ ≈ 0.2 (minimum)
```

### 19.2 Intensités Moyennes sur Confinement

```
u₁ (mosquito→humain) : moyenne = 0.7086
  → 70.86% de réduction transmission

u₂ (humain→mosquito) : moyenne = 0.7444
  → 74.44% de réduction transmission

u₃ (suppression mosquito) : moyenne = 0.7086
  → 70.86% de réduction population
```

**Observation :** u₂ > u₁ ≈ u₃
- Isolation cas (u₂) priorisée empiriquement
- Contradictoire à analyse (u₃ seul meilleur)
- Possible raison : u₂ + facile politiquement (quarantine)

---

## PARTIE 20 : ÉTAPES IMPLICITES MODÈLE CONTRÔLE

### 20.1 Hypothèses Non Explicites

1. **Linéarité contrôles** : ℋ suppose u affecte linéairement β ou N_v
   - Réalité : Peut être non-linéaire (ex. u₃ affecte µ_moustique)

2. **Contrôles continus** : u(t) varient continûment
   - Réalité : Interventions souvent "on/off" (confinement jour X vs jour X+1)

3. **Coûts implémentation** : Terme quadratique u² = coûts croissants
   - **Paramètre manquant :** Spécification coûts réels ($/jour u₁, u₂, u₃?)

4. **Immédiateté intervention** : Changement u prend effet immédiatement
   - Réalité : Retards (délai distribution masques, formation agents)
   - **Implicite :** Délais omis = u exécutée jour même décision

5. **Compliance 100%** : Population suit consignes avec effectiveness u
   - Réalité : Comportement humain imprévisible
   - **Implicite :** U_observé ≠ u_proclamé (ex. u₃ ≠ efficacité réelle spray)

### 20.2 Choix Non Justifiés

1. **Poids p_sj dans L :** Pourquoi certains groupes plus pondérés?
   - Document : silence total
   - Hypothèse : Poids proportionnel population? Cas initiaux? Uniformes?

2. **Facteurs coûts p_{k+1}, p_{k+2}, p_{k+3}** :
   - Non spécifiés numériquement
   - Implicite : Peut être calibré post-hoc pour recréer trajectoires observées

3. **Borne contrôle u_min=0.2, u_max=0.8** :
   - Pourquoi pas [0, 1]? Justification = "réalisme"
   - Implicite : Négoce avec faisabilité politique/logistique

---

## PARTIE 21 : PROBLÈMES ET AMBIGUÏTÉS

### 21.1 Modèle Biologique

**Problème 1 :** Asymptomatiques pas dans objectif
- A_sj contribuent fortement transmission (même transmission rate que I_sj)
- Mais ignorées dans L = Minimisation cases VISIBLES
- **Conséquence :** Stratégies optimales sous-contrôlent réelle transmission

**Problème 2 :** IRR constants
- Implicite : Risque relatif fixe dans temps
- Réalité : IRR peut changer (comportement adaptatif, immunité partielle)

**Problème 3 :** Pas de vaccination
- Modèle admit limitation : "Ixchiq vaccine approuvé 2023 mais non modélisé"
- **Modèle incomplet** pour 2025+ prospective

**Problème 4 :** Mélange complet (homogeneous mixing)
- Pop Foshan 3,800 km² = vraiment homogène?
- Implicite : Pas de structure spatiale sous-districts

### 21.2 Données et Calibration

**Problème 5 :** IRR sources
- Tableau S1 (non fourni) = clé
- Implicite : Calculé de données empiriques Foshan
- **Manquant :** Sensitivité sur IRR estimation? Intervalles confiance?

**Problème 6 :** Cas asymptomatiques non comptabilisés
- Données = cas DIAGNOSTIQUÉS (symptomatiques surtout)
- Non observable : A_sj population
- **Conséquence :** Estimation ℛ₀ biaisée vers symptomatique?

**Problème 7 :** Retards diagnostiques omis
- Cas rapportés par date symptôme (bon!)
- Mais symptôme→diagnostic = 1-2 jours en réalité
- **Implicite :** Aucun délai de reporting modélisé

### 21.3 Paramètres Sensibles

| Paramètre | Valeur | Plage doc | Sensitivité |
|-----------|--------|-----------|-------------|
| q (asympto prob) | 0.155 | 0.03-0.28 | **Très haute** pour ℛ₀ |
| x (mosquito ratio) | 5-15 | - | Pivot N_v |
| a (natalité mosquito) | 0.145 | 0.02-0.27 | **Très haute** |
| ϖ (EIP rate) | 1/5.5 | 1/8.2-1/3 | Modéré |

---

## PARTIE 22 : RÉSOLUTIONS IMPLICITES CONTRÔLES

### 22.1 Résolution Temporelle Contrôles

**Rapportée :** Trajectoires u₁(t), u₂(t), u₃(t) lisses sur [19Jul, 18Sep]
**Implicite :** Dérivée du-HMC sur grille journalière (Δt = 1 jour)
**Non discuté :** Peut-on résoudre contrôles plus finement (horaires)?

### 22.2 Résolution Spatiale

**Modèle :** 0D (pas de structure spatiale)
**Implicite :** Tous groupes âge-sexe mélangés homohumainement
**Conséquence :** Impossibilité capturer spillover entre districts

### 22.3 Résolution Démographique

**Groupes :** 3 âges × 2 sexes = 6 groupes
**Implicite :** Choix k=3 non justifié vs k=2,4,5...
**Sensibilité :** Pas analysée dans document

---

Fin PARTIE 2
À suivre : PARTIE 3 (Pipeline complet + Pseudo-code + Implémentation Python)
