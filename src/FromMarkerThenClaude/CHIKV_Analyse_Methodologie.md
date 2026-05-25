# ANALYSE MÉTHODOLOGIQUE EXHAUSTIVE
## Publication : Transmission and Strategy Analysis of Chikungunya 
### (Foshan 2025 - Modèle SEIAR structuré sexe/âge)

---

## PARTIE 1 : STRUCTURE GLOBALE DU MODÈLE

### 1.1 Architecture Générale

**Deux populations interactives :**

```
HUMAINS (10k compartiments)
├─ k groupes d'âge
└─ Pour chaque groupe j ∈ {1,...,k} et sexe s ∈ {M,F}:
   ├─ S_sj  : Susceptibles
   ├─ E_sj  : Exposés (latents, non-infectieux)
   ├─ I_sj  : Infectieux symptomatiques
   ├─ A_sj  : Infectieux asymptomatiques
   └─ R_sj  : Recovered/Immunisés

MOUSTIQUES (5 compartiments)
├─ Stade larvaire (aquatique):
│  ├─ S_a   : Larves susceptibles
│  └─ I_a   : Larves infectées (transmission verticale)
└─ Stade adulte:
   ├─ S_v   : Adultes susceptibles
   ├─ E_v   : Adultes exposés (incubation extrinsèque)
   └─ I_v   : Adultes infectieux
```

**Paramètres structurels clés :**
- k = 3 groupes d'âge (0-14, 15-59, 60+)
- Taille pop humaine : N_p = Σ(S_mj + E_mj + I_mj + A_mj + R_mj + S_fj + E_fj + I_fj + A_fj + R_fj)
- Taille pop moustiques : N_v = x·N_p (où x = ratio mosquito/humain, estimé 5-15)
- Total compartiments : 10k + 5 = 35 (pour k=3)

---

## PARTIE 2 : SYSTÈME D'ÉQUATIONS DIFFÉRENTIELLES (Modèle 1)

### 2.1 Équations Humains - Groupe d'âge j, Sexe m (mâles)

```
dS_mj/dt = -(β_vp · IRR_mj · S_mj · I_v) / N_p

dE_mj/dt = (β_vp · IRR_mj · S_mj · I_v) / N_p - q·ω'·E_mj - (1-q)·ω·E_mj

dI_mj/dt = (1-q)·ω·E_mj - γ·I_mj

dA_mj/dt = q·ω'·E_mj - γ'·A_mj

dR_mj/dt = γ·I_mj + γ'·A_mj
```

### 2.2 Équations Humains - Groupe d'âge j, Sexe f (femelles)

```
dS_fj/dt = -(β_vp · IRR_fj · S_fj · I_v) / N_p

dE_fj/dt = (β_vp · IRR_fj · S_fj · I_v) / N_p - q·ω'·E_fj - (1-q)·ω·E_fj

dI_fj/dt = (1-q)·ω·E_fj - γ·I_fj

dA_fj/dt = q·ω'·E_fj - γ'·A_fj

dR_fj/dt = γ·I_fj + γ'·A_fj
```

### 2.3 Équations Moustiques - Stade Larvaire

```
dS_a/dt = a·c(t)·(N_v - n·I_a) - λ·S_a

dI_a/dt = a·c(t)·n·I_a - λ·I_a
```

**Fonction saisonnière :**
```
c(t) = cos((t - τ)/T · 2π)
où : τ = 30 jours (phase), T = 365 jours (période annuelle)
```

### 2.4 Équations Moustiques - Stade Adulte

```
dS_v/dt = λ·S_a - (β_pv·S_v·Σ_j(I_mj + I_fj + A_mj + A_fj))/N_p - d·S_v

dE_v/dt = (β_pv·S_v·Σ_j(I_mj + I_fj + A_mj + A_fj))/N_p - (d + ϖ)·E_v

dI_v/dt = λ·I_a + ϖ·E_v - d·I_v
```

---

## PARTIE 3 : PARAMÈTRES ET LEURS VALEURS

### 3.1 Paramètres de Transmission

| Paramètre | Définition | Unité | Valeur | Plage | Source |
|-----------|-----------|-------|-------|-------|--------|
| β_vp | Taux transmission mosquito→humain | jour⁻¹ | À estimer | 0-1 | PMCMC |
| β_pv | Taux transmission humain→mosquito | jour⁻¹ | À estimer | 0-1 | PMCMC |
| IRR_sj | Incidence Rate Ratio (sexe/âge) | - | Voir Tableau S1 | - | Données empiriques |

**IRR : Rapports de risque relatif**
- Baseline : IRR_m1 (hommes 0-14 ans) = 1.0
- Autres groupes : multiplicateurs basés sur l'analyse de l'épidémie Foshan 2025

### 3.2 Paramètres d'Incubation Humaine

| Paramètre | Définition | Valeur | Plage | Source |
|-----------|-----------|--------|-------|--------|
| q | Proportion → asymptomatique | 0.155 | 0.03-0.28 | Littérature |
| ω | Taux latence → symptomatique | 1/4.5 jour⁻¹ | 1/7 à 0.5 jour⁻¹ | Littérature |
| ω' | Taux latence → asymptomatique | 1/4.5 jour⁻¹ | 1/7 à 0.5 jour⁻¹ | Littérature |
| γ | Taux guérison symptomatique | 1/7 jour⁻¹ | - | Littérature |
| γ' | Taux guérison asymptomatique | 1/7 jour⁻¹ | - | Littérature |

**Interprétation :**
- Période latence moyenne : 4.5 jours
- Durée infectiosité : 7 jours (symptomatiques et asymptomatiques)
- Probabilité asymptomatique : 15.5%
- Período latence moustique (extrinsèque) : 5.5 jours

### 3.3 Paramètres Dynamique Moustique

| Paramètre | Définition | Valeur | Plage | Source |
|-----------|-----------|--------|-------|--------|
| a | Taux natalité moustique | 0.145 jour⁻¹ | 0.02-0.27 | Littérature |
| λ | Taux émergence larvaire | 0.0902 jour⁻¹ | 0.0691-0.1296 | Littérature |
| d | Taux mortalité naturelle moustique | 1/7.4 jour⁻¹ | 1/9.8-1/4.5 | Littérature |
| ϖ | Taux incubation extrinsèque | 1/5.5 jour⁻¹ | 1/8.2-1/3 | Littérature |
| n | Taux transmission verticale | 0.0181 | 0.0076-0.0286 | Littérature |
| x | Ratio moustiques/humains | À estimer | 5-15 | PMCMC |

---

## PARTIE 4 : NOMBRE DE REPRODUCTION DE BASE (ℛ₀)

### 4.1 Définition Théorique

ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))

Deux composantes multiplicatives :
- **ℛ₀(vp)** : Nombre infections secondaires humaines par moustique infecté
- **ℛ₀(pv)** : Nombre moustiques infectés par humain infecté

### 4.2 Décomposition ℛ₀(vp) - Chemin Mosquito→Humain

```
ℛ₀(vp) = Σ_j [ ℛ₀(vp·I_m·j) + ℛ₀(vp·A_m·j) + ℛ₀(vp·I_f·j) + ℛ₀(vp·A_f·j) ]

Où chaque composante :

ℛ₀(vp·I_m·j) = [β_vp·IRR_mj·S_mj0·(1-q)·ω] / [N_p·γ·(q·ω' + (1-q)·ω)]
                (Infections symptomatiques mâles groupe j)

ℛ₀(vp·A_m·j) = [β_vp·IRR_mj·S_mj0·q·ω'] / [N_p·γ'·(q·ω' + (1-q)·ω)]
                (Infections asymptomatiques mâles groupe j)

Idem pour femelles (f)
```

### 4.3 Décomposition ℛ₀(pv) - Chemin Humain→Mosquito

```
ℛ₀(pv) = (β_pv·S_v0·ϖ) / [N_p·(d + ϖ)·d]

Interprétation :
- β_pv : efficacité transmission humain→mosquito
- S_v0 : Moustiques susceptibles à l'équilibre
- ϖ/(d+ϖ) : Proportion larves qui deviennent adultes infectieuses
- ϖ/d : Durée vida infectieuse moustique
```

### 4.4 Valeurs Empiriques (Épidémie Foshan 2025)

| Période | ℛ₀ Total | ℛ₀(vp) | ℛ₀(pv) | Interprétation |
|---------|----------|--------|--------|-----------------|
| 11 Jun-18 Jul (Préparation) | 10.1235 | 3.6197 | 28.3132 | **Explosif** (vp << pv) |
| 19 Jul-18 Sep (Confinement) | 1.3865 | 0.8665 | 2.2185 | **Contrôlé** (ℛ₀ < 1 équivalent) |
| 19-25 Jul (Décalage incubation) | 1.2934 | 1.0341 | 1.6178 | Transition phase |
| 26 Jul-18 Sep (Post-décalage) | 1.3243 | 0.8122 | 2.1593 | Persistance mosquitos |

**Observations critiques :**
- Phase préparation : transmission humain→mosquito **8x** plus intense que mosquito→humain !
- Les asymptomatiques (surtout hommes 15-59) contribuent plus que symptomatiques
- Femmes 60+ : reproduction basale très faible (risque faible)

---

## PARTIE 5 : HYPOTHÈSES MODÈLE

### 5.1 Hypothèses Biologiques

1. **Transmission unique inter-espèces** : Pas de transmission H2H directe, pas de V2V

2. **Structure par sexe-âge** : Transmission différentielle (IRR) par groupe démographique

3. **Probabilité asymptomatique constante** : q = 15.5% quelque soit l'âge/sexe

4. **Transmission verticale moustique** : n proportion larves naissent infectées
   - Mécanisme : Virémie dans gonades mère

5. **Saisonnalité** : Dynamique moustique suit cycle cosinus annuel
   - Pic : environ jour 30 + 365/4 ≈ jour 121 (mai)
   - Creux : environ jour 30 + 3·365/4 ≈ jour 304 (novembre)

6. **Population humaine constante** : N_p constant (pas de natalité/mortalité humaine)

7. **Immunité permanente** : Infection confère immunité durable

### 5.2 Hypothèses Méthodologiques

1. **Équilibre vie pour moustiques** : Moyenne 7.4 jours
2. **Incubation extrinsèque** : 5.5 jours en moyenne
3. **Ratio moustiques/humains** : Fluctue mais stabilisé par la dynamique larvaire

---

## PARTIE 6 : PROCESSUS D'ESTIMATION PARAMÉTRIQUE

### 6.1 Méthode PMCMC (Particle Markov Chain Monte Carlo)

**Framework Bayésien :**

```
Posterior ∝ Likelihood × Prior
p(θ|y₁:ₜ) ∝ p(y₁:ₜ|θ) · p(θ)
```

**Algorithme Metropolis-Hastings :**

1. À l'itération k :
   - Générer θ* de q(θ|θ^(k-1)) ~ N(θ^(k-1), Σ)
   
2. Invoquer **Particle Filter** pour estimer :
   ```
   p̂(y₁:ₜ|θ*) = ∏ₜ₌₁ᵀ [N⁻¹ Σᵢ₌₁ᴺ w_t^(i)]
   ```
   (Moyenne pondérée de N particules)
   
3. Calculer probabilité acceptation :
   ```
   α = min{1, [p̂(y₁:ₜ|θ*)·p(θ*)/p(θ^(k-1))] · [q(θ^(k-1)|θ*)/q(θ*|θ^(k-1))]}
   ```
   
4. Si uniform(0,1) < α : accepter θ*, sinon garder θ^(k-1)

5. Après burn-in : {θ^(k)}_{k>K_burn} ~ p(θ|y₁:ₜ)

**Estimation point :** Moyenne postérieure E[θ|y₁:ₜ] ou mode

---

## PARTIE 7 : ANALYSE DU NOMBRE REPRODUCTION DE BASE (NEXT-GEN MATRIX)

### 7.1 Matrice de Génération Suivante

**État sans maladie (DFE) :**
```
E₀ = (S_m10, 0, 0, S_m20, 0, 0, ..., S_m30, 0, 0, 
      S_f10, 0, 0, ..., S_f30, 0, 0, 
      S_a0, 0, S_v0, 0, I_v0)
```
Où : N_p = Σ(S_mj0 + S_fj0), N_v = S_a0 + S_v0

### 7.2 Jacobienne Matrice F (Nouveaux infectés)

Au DFE : F se décompose en blocs
```
F(E₀) = [ 0_{6k×6k}      F₁ ]
        [ F₂             0_{2×2} ]
```

F₁ : Transmissions moustique→humain (dimension 6k × 2)
F₂ : Transmissions humain→moustique (dimension 2 × 6k)

### 7.3 Jacobienne Matrice V (Flux sortants)

```
V(E₀) = [ V₁                0_{6k×2} ]
        [ 0_{2×6k}          V₂ ]

Où :
V₁ = I_{2k} ⊗ [ q·ω' + (1-q)·ω    0    0 ]
              [ -(1-q)·ω          γ    0 ]
              [ -q·ω'             0    γ' ]

V₂ = [ (d+ϖ)    0  ]
     [ -ϖ       d  ]
```

### 7.4 Calcul ℛ₀ = ρ(FV⁻¹(E₀))

Rayon spectral = plus grande valeur propre

**Pour ce modèle :**
```
ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))
```

C'est la **racine géométrique** ! (Non additive)

**Raison biologique :** Transmission cyclique : 
Humain→Moustique→Humain (2 étapes = géométrique)

---

## PARTIE 8 : PHASES ÉPIDÉMIOLOGIQUES FOSHAN 2025

### 8.1 Chronologie

```
16 Jun 2025         Cas importé détecté
        |
        ├─────── PHASE PRÉPARATION ───────┤
        |        (Routine → Urgence)       |
        |        - Juin 16                 |
        |        - Juillet 18              |
        |    9,929 cas cumulatifs (9 sep)  |
        |
    18 Jui | Pic 405 cas/jour (Jul 18)
        |
    19 Jul TRANSITION (Mesures confinement)
        |
        ├──── PHASE CONFINEMENT ──────────┤
        |                                   |
        ├─ Décalage incubation (19-25 Jul) |
        |  (Effet période latence)         |
        |                                   |
        ├─ Post-décalage (26 Jul-18 Sep)   |
        |  Pic 493 cas/jour (Jul 28)       |
        |  Déclin progressif (Aug-Sep)     |
        |                                   
   18 Sep Fin observation
```

### 8.2 Compositions Démographiques

**Phase Préparation (16 Jun-18 Jul) :**
- Hommes : 51.09%
  - 15-59 ans : 32.46% des cas
  - 60+ ans : 11.06%
- Femmes : 48.91%
  - 15-59 ans : 30.03%

**Phase Confinement (19 Jul-18 Sep) :**
- Hommes : 52.39%
- Femmes : 47.61%
- 15-59 ans : **groupe le plus impacté dans les deux phases**

---

## PARTIE 9 : PRETRAITEMENT ET NETTOYAGE DONNÉES

### 9.1 Source Données

- **WHO** : Rapports épidémiques globaux (Sept 2025)
- **Bureau Municipalités Foshan** : Démographie population
- **Ministères Santé** : Cas confirmés vs suspects
- **Données empiriques Épidémie** : Symptom onset date (symptôme, pas diagnose)

### 9.2 Nettoyage et Stratification

```
Données brutes (WHO/Ministères)
    ↓
[Filtrage] : Retirer records incomplets (date symptôme manquante)
    ↓
[Stratification] : 
  - Sex : M / F
  - Age : 0-14 / 15-59 / 60+
  - Status : Cas confirmé / suspect
    ↓
[Normalisation dates] : Date symptôme → Date diagnostic (décalage ~1-2 jours)
    ↓
[Segmentation temporelle] :
  - Période 1 : 16 Jun - 18 Jul (avant confinement)
  - Période 2a : 19 Jul - 25 Jul (décalage incubation)
  - Période 2b : 26 Jul - 18 Sep (post-décalage)
```

### 9.3 Construction Série Chronologique

```
For each day t from 16 Jun to 18 Sep:
  - Compter cas avec symptom onset = t
  - Stratifier par (sexe, âge)
  - Créer vecteur y_t = [y_m0(t), y_m1(t), y_m2(t), 
                          y_f0(t), y_f1(t), y_f2(t)]
  - Appliquer filtre lisse (mobile average optionnelle)
```

### 9.4 Masques QA (Quality Assurance)

**Critères validité :**
1. Date symptôme ≤ Date diagnostic
2. Age ∈ [0, 120]
3. Sexe ∈ {M, F}
4. Cas confirmés ≤ Cas totaux
5. Pas de doublons (ID unique)

**Actions :**
- Retirer si date symptôme manquante
- Retirer si age > 100 (erreur transcription probable)
- Imputer sexe manquant : ratio observé M/F
- Flaguer for manual review : age non catégorisé (1-14 vs 15-59 ambigu)

---

## PARTIE 10 : INTÉGRATION NUMÉRIQUE

### 10.1 Méthode Runge-Kutta d'Ordre 4

```
État : x_t = [S_m1, E_m1, I_m1, A_m1, R_m1, ..., I_v]ᵀ (35 variables)

Pour t = 0 à T_final, pas = Δt :

  k1 = f(t, x_t)
  k2 = f(t + Δt/2, x_t + k1·Δt/2)
  k3 = f(t + Δt/2, x_t + k2·Δt/2)
  k4 = f(t + Δt, x_t + k3·Δt)
  
  x_{t+Δt} = x_t + (k1 + 2·k2 + 2·k3 + k4)·Δt/6
```

**Paramètres :**
- Δt = 0.01 jour (précision requise pour dynamiques rapides)
- T_final = 95 jours (16 Jun à 18 Sep)

### 10.2 Conditions Initiales

**État initial DFE quasi-perturbé :**
```
S_mj(0) = N_p · p_m · frac_j - (E_mj(0) + I_mj(0) + A_mj(0))
S_fj(0) = N_p · p_f · frac_j - (E_fj(0) + I_fj(0) + A_fj(0))

Où :
  p_m, p_f = proportion sexe dans pop
  frac_j = proportion groupe âge j
  
E_mj(0), I_mj(0), A_mj(0) : estimés à partir 1ers cas
  (typiquement : ~10-20 exposés, ~1-2 infectés)
```

---

## PARTIE 11 : ÉTAPES IMPLICITES NON DOCUMENTÉES

### 11.1 Calibration IRR

**Procédure déduite :**
1. Calculer taux incidence brut par groupe : Incidence_sj = Cas_sj / Pop_sj
2. Définir groupe de référence : Males 0-14 = 1.0
3. Calculer ratio : IRR_sj = Incidence_sj / Incidence_m0
4. Lisser si bruitées (moyenne mobile 3-jours ?)

**Implicite :** Incidence basée sur **cas confirmés / population estimée**
- Population → à partir données Foshan 2025 (âge-sexe distributions)

### 11.2 Normalisation Population

N_p traité constant :
- Initialisé jour 1 : N_p(0) = population Foshan 2025
- Aucune natalité / mortalité humaine
- Justification : Période 3 mois, impact démographique négligeable

### 11.3 Filtrage Série Temporelle

**Implicite :** Lissage potentiel des données cas avant fitting
- Raison : Observations bruitées (weekend effects, retards diag)
- Probable : Moyenne mobile 3-7 jours OU spline lisse

### 11.4 Sélection Groupes Âge

k=3 choix :
- 0-14 : Enfants/ados (faible mobilité professionnelle)
- 15-59 : Actifs (haute exposition)
- 60+ : Retraités/âgés (mobilité différente)

**Implicite :** Validation sensitivité k=2 (0-14, 15+) vs k=4 (0-14, 15-30, 30-60, 60+)?
Document ne discute pas cette décision...

---

## PARTIE 12 : RÉSOLUTIONS SPATIALES ET TEMPORELLES

### 12.1 Résolution Spatiale

**Niveau :** Ville Foshan (pas de sous-régions)
- Aire : ~3,798 km²
- Pop : ~7.3 millions (2025 estimation)
- Modèle homogène = **mélange complet supposé**

**Implicite :** 
- Tous groupes spatialement mélangés
- Pas de sous-modèles par district
- Justification : Durée courte, transport rapide

### 12.2 Résolution Temporelle

**Granularité :** Journalière (rapportée)
- Incubation humaine : 4.5 jours
- Extrinsèque moustique : 5.5 jours
- Simulation numériques : Δt = 0.01 jour (100x plus fine)

**Cycles :** Saisonnier + circadien
- Saisonnier : cos((t-30)/365 · 2π) [modélise pic/creux annuels]
- Circadien : **IMPLICITE dans taux bites moustiques** (non explicité)

---

## PARTIE 13 : CALIBRATION TEMPÉRATURE-SAISON

### 13.1 Fonction Saisonnière

```
c(t) = cos( (t - τ) / T · 2π )

τ = 30 jours  (phase: pic début février?)
T = 365 jours (période annuelle)

Effet : Module
  - Taux natalité moustique a·c(t)
  - Transmission verticale a·c(t)·n
```

**Interprétation :**
- Jour t=30 : c(30) = cos(0) = 1.0 → max transmission
- Jour t=122 : c(122) = cos(π/2) ≈ 0 → min transmission
- Jour t=213 : c(213) = cos(π) = -1.0 → min (≈ été)

**Observation :** Cela correspond à climathologie Guangdong
- Été (Jun-Aug) : Haute densité moustique (pluies, chaleur)
- Phase décalée τ=30 : ??? (non justifiée)

### 13.2 Lien Température Non Modélisé

**Limitation documentée :** "Le modèle ne prend PAS en compte changement climat"
- Température → affects durée EIP (extrinsic incubation)
- Température → affects survie moustique
- Température → affects fécondité

**Implicite :** Paramètres (d, ω_v, a) sont constants
- Devrait varier T(t) selon Foshan 2025 température
- **Paramètre manquant clé :** Series temporelle T_min(t), T_max(t), RH(t)

---

Fin PARTIE 1
À suivre : PARTIE 2 (Modèle Contrôle Optimal) et PARTIE 3 (Pseudo-code + Implémentation)
