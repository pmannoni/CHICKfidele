# ANALYSE COMPARATIVE
## Publication Foshan (Li et al.) vs Publication Nature (Karthik & Ghosh)
### Deux approches du modèle Chikungunya - 2025-2026

---

## 📊 TABLEAU COMPARATIF GLOBAL

| Critère | **Article 1 : Foshan** (Li et al.) | **Article 2 : Nature** (Karthik & Ghosh) |
|---------|----------------------------------|-------------------------------------|
| **Titre** | Transmission and strategy analysis... | A mathematical approach to Chikungunya transmission dynamics incorporating media awareness... |
| **Lieu d'étude** | Foshan, Guangdong, Chine | Inde (National + 3 états) |
| **Journal** | ❓ Non spécifié | Scientific Reports (Nature) |
| **Année publication** | 2025 | 14 Mars 2026 |
| **Épidémie analysée** | Épidémie 2025 Foshan (9,929 cas) | Données cumulées 2015-2024 Inde |
| **Période données** | 16 Jun - 18 Sep 2025 (95j) | 10 ans (2015-2024) |

---

## 🏗️ COMPARAISON STRUCTURE MODÈLE

### Article 1 - Foshan (Li et al.)

**Compartiments :**
```
HUMAINS (30):
├─ 3 âges (0-14, 15-59, 60+) × 2 sexes
├─ 5 comparts (S, E, I_symp, A_asymp, R)
└─ TOTAL = 30

MOUSTIQUES (5):
├─ Larves (S_a, I_a)
├─ Adultes (S_v, E_v, I_v)
└─ TOTAL = 5

GRAND TOTAL = 35 variables
```

**Caractéristiques :**
- ✅ Structure **sexe-âge explicite** (6 groupes démographiques)
- ✅ Dynamique **larves + adultes** (cycle complet moustique)
- ✅ Transmission **verticale** moustiques (n=0.0181)
- ✅ Saisonnalité **cosinus** (τ=30, T=365)
- ❌ **PAS de compartiment awareness/média**

### Article 2 - Nature (Karthik & Ghosh)

**Compartiments :**
```
HUMAINS (7):
├─ S_u (Susceptibles sans awareness)
├─ S_a (Susceptibles avec awareness)
├─ E_h (Exposés)
├─ I_a (Infectieux asymptomatiques)
├─ I_s (Infectieux symptomatiques)
├─ R (Recovered)
└─ M (Media/Awareness compartment)

MOUSTIQUES (3):
├─ S_v (Susceptibles)
├─ E_v (Exposés)
└─ I_v (Infectieux)

GRAND TOTAL = 10 variables
```

**Caractéristiques :**
- ❌ **PAS de structure sexe-âge** (agrégé)
- ❌ **Moustiques adultes uniquement** (pas larves)
- ❌ **Pas de transmission verticale**
- ✅ **Compartiment awareness explicite (M)** ← UNIQUE
- ✅ Plus **simple et parcimonieux** (10 vs 35)

---

## 🔍 COMPARAISON PARAMÈTRES CLÉS

### Transmission Mosquito→Humain (β_vp vs β)

| Aspect | Foshan | Nature |
|--------|--------|--------|
| **Notation** | β_vp | β (global) |
| **Valeur** | À estimer (PMCMC) | À estimer (MLE) |
| **Hétérogénéité** | Par groupe (IRR_sj) | Uniforme (pas groupes) |
| **Probabilité transmission** | Implicite β_vp | Explicite b,c,d,e (4 params) |

**Formula transmission (unaware → infectious mosquito) :**
```
Foshan:  (1-u₁)·β_vp·IRR_mj·S_mj·I_v / N_p
Nature:  (1-u₁(t))·b·β·S_u·I_v / N_h
```

### Incubation Humaine

| Paramètre | Foshan | Nature |
|-----------|--------|--------|
| **ω (E→I_symp)** | 1/4.5 jour⁻¹ | ε = ? (à Table) |
| **ω' (E→A_asymp)** | 1/4.5 jour⁻¹ | ε = ? (same) |
| **Probabilité asympto (q)** | 0.155 | κ (à Table) |
| **Durée infectieuse (γ)** | 1/7 jour⁻¹ | γ, α (asymp/symp différents) |

### Dynamique Moustique

| Aspect | Foshan | Nature |
|--------|--------|--------|
| **Stade larvaire** | ✅ Modélisé (S_a, I_a) | ❌ Omis |
| **Natalité moustique (a)** | 0.145 jour⁻¹ | Λ_v (recruitment) |
| **Saisonnalité** | c(t) = cos(...) | ❌ NON modélisée |
| **Transmission verticale** | n = 0.0181 | ❌ NON modélisée |
| **EIP (ϖ)** | 1/5.5 jour⁻¹ | ρ (à Table) |
| **Mortalité (μ_v)** | 1/7.4 jour⁻¹ | μ_v (à Table) |

### Paramètres Awareness (UNIQUE à Nature)

| Paramètre | Foshan | Nature |
|-----------|--------|--------|
| **Compartiment M** | ❌ ABSENT | ✅ M (Density of awareness) |
| **Réduction risk η** | Implicite | (1-η)·β dans formules |
| **Génération awareness (τ)** | Non applicable | τ (rate from I_s→M) |
| **Décay awareness (δ)** | Non applicable | δ₀ (decay rate) |
| **Transformation S_u→S_a** | ❌ Pas | σ·M (transition rate) |

---

## 🔬 COMPARAISON MÉTHODOLOGIE

### 1️⃣ ESTIMATION PARAMÈTRES

**Foshan (Li et al.) :**
```
Méthode: PMCMC (Particle Markov Chain Monte Carlo)
├─ Particle Filter pour likelihood
├─ Metropolis-Hastings MCMC
├─ Phase 1: Estimé (Préparation 16 Jun-18 Jul)
├─ Phase 2: Appliqué (Confinement 19 Jul-18 Sep)
└─ Paramètres: β_vp, β_pv, x, IRR_sj
```

**Nature (Karthik & Ghosh) :**
```
Méthode: MLE (Maximum Likelihood Estimation)
├─ Cumulative case data fitting
├─ Python implementation
├─ Données: 2015-2024 (10 ans)
├─ Régions: Inde + 3 états
└─ Paramètres: β, b, c, d, e, ε, κ, α, γ, ...
```

**Différence clé :** 
- Foshan = PMCMC + time-series daily cases (plus avancé)
- Nature = MLE + cumulative data (standard mais moins détaillé)

### 2️⃣ NOMBRE REPRODUCTION BASE (ℛ₀)

**Foshan :**
```
ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))
├─ Décomposition par groupe démographique
├─ Distinction symptomatique vs asymptomatique
├─ Valeurs empiriques:
│  ├─ Phase prep: 10.12 (EXPLOSIF)
│  └─ Phase confin: 1.39 (CONTRÔLÉ)
└─ Sensibilité q, x, a TRÈS ÉLEVÉE
```

**Nature :**
```
ℛ₀ = √[ρ·b·β/(μ_v(μ_v+ρ)) · (Λ_v·d·β·ε·κ·μ)/(Λ_h·μ_v·(ε+μ)·(γ+μ₁+μ)) 
     + (Λ_v·e·β·ε·μ·(κ-1))/(Λ_h·μ_v·(ε+μ)·(α+μ₂+μ))]

├─ Formule PLUS COMPLEXE (implicite β)
├─ Pas de décomposition démographique
└─ Valeurs India: R₀ ≈ ? (Voir Table 1)
```

**Verdict :**
- Foshan = **Décomposition plus transparente** (vp, pv séparés)
- Nature = **Formule intégrée plus compacte**

### 3️⃣ ANALYSE SENSIBILITÉ

**Foshan :**
```
Paramètres testés: q, x, a (implicitement)
Résultat: q, a TRÈS sensibles → model "weakly robust"
Tableau S7 → Plages sensibilité documentées
```

**Nature :**
```
✅ COMPLET :
├─ Normalized forward sensitivity index
├─ Tous paramètres analysés
├─ Figure 3: Visualisation complète par région
├─ Table 4: Résumé indices sensibilité
└─ Identification: β, b, Λ_v CRITIQUES
```

**Verdict :**
- Nature = **Plus systématique et documenté**
- Foshan = **Partiel mais suffisant pour objectifs**

### 4️⃣ VALIDITÉ MODÈLE

**Foshan :**
```
Métriques : RSS, Goodness-of-fit (implicite)
Problème: AIC/BIC non rapportés
Comparaison: Non testée (k=2,4,5)
Sensibilité cross-validation: ABSENT
```

**Nature :**
```
✅ Complet:
├─ R² (coefficient détermination)
├─ RMSE (root mean square error)
├─ AIC (Akaike Information Criterion)
├─ Tableau 3: Summary validation metrics
└─ Résultats: R²=0.99+, RMSE très bas
```

**Verdict :**
- Nature = **Validation bien documentée**
- Foshan = **Manquements critiques**

---

## 🎯 COMPARAISON CONTRÔLE OPTIMAL

### Foshan (Li et al.)

**Contrôles :**
```
u₁ : Mosquito→Human transmission (masques, répellent)
u₂ : Human→Mosquito transmission (isolement)
u₃ : Mosquito population suppression (spray, filets)

Nombre: 3 contrôles
Bounds: 0.2 ≤ u_i ≤ 0.8
```

**Framework :**
```
Hamiltonien: ℋ = L + Σ ηᵢ·fᵢ
Adjoint: 35 équations (couplées)
Method: Forward-Backward Sweep
Objectif: min(Σ p_sj·I_sj + coûts u²)
```

**Résultats :**
```
Meilleur seul: u₃ = 78.5%
Meilleur pair: u₁+u₃ = 81.5%
Optimal tous 3: u₁+u₂+u₃ = 95.8%

Asymmetric strategies:
├─ (0.6, 0.8, 0.9) → R_eff = 0.9055
└─ (0.1, 0.9, 0.9) → R_eff = 0.9604
```

### Nature (Karthik & Ghosh)

**Contrôles :**
```
u₁ : Reduction of transmission (personal protective measures)
u₂ : Enhancement of treatment (augmented recovery)

Nombre: 2 contrôles (MOINS QUE FOSHAN)
Bounds: 0 ≤ u_i < 1
```

**Framework :**
```
Hamiltonien: ℋ = L + Σ λᵢ·(∂/∂state)
Adjoint: 10 équations (plus simple)
Method: Forward-Backward Sweep (MATLAB)
Objectif: min(C₁I_a + C₂I_s + C₃I_v + coûts u²)
```

**Résultats :**
```
Strategy A (u₁ only): Significant reduction I_s
Strategy B (u₂ only): Consistent reduction vs no control
Strategy A+B: "Most significant decrease in symptomatic infections"

Quantification: VAGUE (pas de %)
```

**Verdict :**
- Foshan = **3 contrôles, analyses systématiques (8 scénarios)**
- Nature = **2 contrôles, moins quantifié**

---

## 📈 COMPARAISON DONNÉES & VALIDATION EMPIRIQUE

### Foshan (Li et al.)

**Source données :**
```
WHO epidemiological data + Ministry Health Foshan
Période: 16 Jun - 18 Sep 2025 (court, 95j)
Cas: 9,929 confirmés
Granularité: Journalière par groupe (sexe-âge)
Stratification: 6 groupes × 2 phases
```

**Validation :**
```
Fitting: Figure 3 (comparaison courbes observés vs simulés)
Métriques: ❌ AIC/BIC/RMSE NON RAPPORTÉS
Qualité: Visual match acceptable mais non quantifié
```

### Nature (Karthik & Ghosh)

**Source données :**
```
IndiaStat database (official India statistics)
Période: 2015-2024 (long, 10 ans)
Cas: Cumulés par région
Granularité: Annuelle
Régions: Inde (national) + Gujarat, Karnataka, Maharashtra
```

**Validation :**
```
Fitting: Figure 2 (fitted curves + 95% CI)
Métriques: ✅ COMPLET
├─ R² (0.99+ range)
├─ RMSE (très bas)
├─ AIC (reporté)
└─ Tableau 3: Summary validation metrics
```

**Verdict :**
- Foshan = **Données temporelles fines mais validation incomplète**
- Nature = **Données agrégées mais validation robuste**

---

## 🌍 COMPARAISON APPLICABILITÉ & IMPACT

### Foshan (Li et al.)

**Contexte :**
```
✅ Largement applicable:
├─ Épidémie réelle (données empiriques)
├─ Structure démographique détaillée
├─ Framework transférable autres pays
└─ Contrôles réalistes (3 voies)

❌ Limitations:
├─ Données courtes (95 jours)
├─ Chine spécifique (demography, climate)
├─ Pas de validation long-term
└─ Ambiguïtés paramétriques (5 Tier-1)
```

**Utilité pratique :**
```
Excellente pour: 
├─ Évaluation interventions urgentes (outbreak control)
├─ Allocation ressources court-term
└─ Framework transférable dengue/zika

Faible pour:
├─ Planification long-term (10+ ans)
├─ Comparaison inter-régionale
└─ Prédictions sans données locales
```

### Nature (Karthik & Ghosh)

**Contexte :**
```
✅ Généraliste:
├─ 10 ans de données
├─ Multi-région (état-level)
├─ Saisonnalité implicitée
├─ Awareness/média explicité

❌ Limitations:
├─ Pas de structure démographique
├─ Données cumulées (moins détail)
├─ Awareness = proxy simple
└─ Moustiques incomplets (pas larves)
```

**Utilité pratique :**
```
Excellente pour: 
├─ Planification long-term (10 ans)
├─ Tendance nationale
├─ Impact awareness programs
└─ Baseline endemic dynamics

Faible pour:
├─ Épidémies aigues (outbreak response)
├─ Stratégies par groupe démographique
├─ Prédictions fine-grain spatial
```

---

## 🔴 AMBIGUÏTÉS & MANQUEMENTS COMPARÉS

### Foshan (Li et al.)

**Tier 1 - Critiques (5) :**
```
❌ Tableau S1 (IRR détails) MANQUANT
❌ Poids objectif p_sj MANQUANTS
❌ Coûts intervention p_{k+1,2,3} MANQUANTS
❌ Dates transitions u_i imprécises
❌ Poids sexe non-clarifiés
```

**Tier 2-3 - Modérés :**
```
🟡 Choix k=3 âges non-justifié
🟡 Phase saisonnière τ=30 non-justifiée
⚠️ Conditions initiales imprécises
```

### Nature (Karthik & Ghosh)

**Ambiguïtés significatives :**
```
❌ Paramètres awareness (σ, τ, δ) valeurs? Tableau 1/2?
❌ Spécification M compartment dynamics imprécise
❌ Pas de justification pourquoi 2 contrôles (pas 3?)
❌ Poids objectif (C₁, C₂, C₃, C₄, C₅) = ?
   Rapporté: C₁=1, C₂=1, C₃=1, C₄=40, C₅=55
   Question: Calibré comment?
```

**Qualités :**
```
✅ Sensibilité complète (Figure 3)
✅ Validation robuste (Table 3, R²/RMSE/AIC)
✅ Contour plots R₀ (Figure 4-6)
✅ Équations adjoint détaillées
```

**Verdict :**
- Foshan = **Plus manquements Tier 1 (paramétriques)**
- Nature = **Moins manquements mais moins détaillée**

---

## 📊 TABLEAU DÉCISION : LAQUELLE UTILISER?

| Cas d'usage | **Foshan** | **Nature** | Recommandation |
|------------|-----------|-----------|-----------------|
| Épidémie aigüe (outbreak response) | ✅✅✅ | ❌ | **Foshan** |
| Planification 10 ans | ❌ | ✅✅✅ | **Nature** |
| Allocation ressources urgente | ✅✅✅ | ⚠️ | **Foshan** |
| Tendance épidémiologique | ❌ | ✅✅ | **Nature** |
| Impact démographie | ✅✅ | ❌ | **Foshan** |
| Impact awareness/media | ❌ | ✅✅ | **Nature** |
| Validation robustesse | ⚠️ | ✅✅ | **Nature** |
| Reproductibilité complète | ⚠️ (manquements S1-S4) | ✅ | **Nature** |

---

## 🔬 COMPARAISON MÉTHODOLOGIE (TABLEAU SYNTHÈSE)

| Aspect | Foshan | Nature | Winner |
|--------|--------|--------|--------|
| **Complexité modèle** | 35 variables | 10 variables | Nature (simple) |
| **Structure démographique** | Sexe-âge (✅) | Uniforme (❌) | Foshan |
| **Dynamique moustique** | Larves+adultes | Adultes seuls | Foshan |
| **Awareness explicite** | Non | Oui | Nature |
| **Paramètres clés documentés** | Partiels | Complets | Nature |
| **Sensibilité analyse** | Basique | Systématique | Nature |
| **Validation goodness-of-fit** | Visuelle | Statistique | Nature |
| **Contrôles optimaux** | 3 voies | 2 voies | Foshan |
| **Quantification résultats** | Précise (%) | Vague | Foshan |
| **Reproductibilité** | 50% (manquements S) | 80%+ | Nature |
| **Applicabilité géographique** | Large | Inde-spécifique | Foshan |
| **Période données** | Court (95j) | Long (10 ans) | Nature |

---

## 💡 SYNTHÈSE COMPARATIVE

### Forces Foshan (Li et al.)
```
✅ Structure complexe mais réaliste (sexe-âge)
✅ Trois contrôles interventions (comprehensive)
✅ Résultats quantifiés précisément (%)
✅ Données empiriques (épidémie réelle 2025)
✅ Framework transférable (dengue/zika)
```

### Faiblesses Foshan
```
❌ Ambiguïtés paramétriques (Tier 1: 5 manquements)
❌ Validation incomplète (AIC/BIC/RMSE absents)
❌ Données courtes (95 jours)
❌ Pas de compartiment awareness
❌ Reproductibilité partielle (50%)
```

### Forces Nature (Karthik & Ghosh)
```
✅ Compartiment awareness explicite (innovation)
✅ Données longues (10 ans, multi-région)
✅ Validation statistique robuste (Table 3)
✅ Sensibilité complète (Figure 3)
✅ Reproductibilité élevée (80%+)
```

### Faiblesses Nature
```
❌ Structure trop simple (pas sexe-âge)
❌ Moustiques incomplets (pas larves)
❌ Dynamique saisonnière omise
❌ Transmission verticale ignorée
❌ Seulement 2 contrôles
```

---

## 🎯 VERDICT FINAL

### Pour **contrôle urgent** (semaines-mois) :
→ **Foshan meilleur** (données empiriques, 3 contrôles, structure fine)
**Mais** documenter Tableaux S1-S4 d'abord

### Pour **planification stratégique** (années) :
→ **Nature meilleur** (données longues, validation robuste, awareness)
**Mais** ajouter structure démographique

### Pour **comparaison méthodologie** :
→ **Nature + Foshan ensemble** couvrent gaps mutuels
Nature = simple + awareness | Foshan = complexe + démographie

### Recommandation hybride :
```
Modèle idéal = Foshan structure + Nature awareness + Nature validation
```

---

## 📚 RÉFÉRENCES CROISÉES

| Aspect | Ressource Foshan | Ressource Nature |
|--------|------------------|------------------|
| ODEs complètes | Part 1-2 (doc 1) | Eq. 1 (text) |
| ℛ₀ calcul | Part 4 (doc 1) | Methods section |
| Contrôle optimal | Part 14-22 (doc 2) | Optimal control section |
| Données fitting | Part 6-7 (doc 1) | Data fitting, Table 1 |
| Sensibilité | Part 22 (doc 2) | Figure 3, Table 4 |

