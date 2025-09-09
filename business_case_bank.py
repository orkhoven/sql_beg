# Ce script est conçu pour être exécuté avec **Streamlit**.
# Pour le lancer, assurez‑vous d'avoir installé streamlit :
#   pip install streamlit
# puis exécutez dans un terminal :
#   streamlit run nom_du_fichier.py

try:
    import streamlit as st
except ModuleNotFoundError:
    raise RuntimeError(
        "Le module 'streamlit' n'est pas installé dans cet environnement. "
        "Installez-le avec 'pip install streamlit' puis exécutez ce script avec 'streamlit run'."
    )

st.set_page_config(page_title="📘 Bibliothèque – Modélisation & SQL", page_icon="📘", layout="wide")

# --- Helpers ---------------------------------------------------------------
CARD_OPTIONS = [
    "1–1",
    "1–N",
    "N–1",
    "N–N",
]

def score_cardinality(resp, solution):
    return sum(1 for k, v in resp.items() if v == solution[k])

def pct(n, d):
    return 0 if d == 0 else round(n * 100 / d)

# --- UI -------------------------------------------------------------------
st.title("📘 Bibliothèque – Modélisation relationnelle & quiz SQL")
st.markdown(
    """
    **Objectif :** Comprendre le passage **besoin ➜ MCD ➜ MLD**, les **cardinalités**, et vérifier 
    les notions SQL de base via deux mini‑quiz. L'application est **interactive** et pensée pour 
    une pédagogie active (vous expérimentez, vous vérifiez, vous corrigez).
    """
)

with st.expander("🔎 Contexte – Cahier des charges (à lire)", expanded=True):
    st.markdown(
        """
        La bibliothèque municipale gère **des Membres** et **des Livres**. 
        Un Membre peut **emprunter** plusieurs Livres ; un Livre peut être emprunté plusieurs fois, 
        **mais jamais par deux personnes au même moment**. 
        Les Livres sont rattachés à **une ou plusieurs Catégories** (jeunesse, SF, histoire, ...).

        Pour chaque **Emprunt** on mémorise : `date_emprunt`, `date_retour_prevue`, `date_retour` (si rendu), 
        et un `montant_amende` si retard. 

        **Contraintes** : 
        - `email` des membres **unique** ; 
        - `isbn` des livres **unique** ; 
        - un membre peut avoir **au plus 5 emprunts actifs** (retour non enregistré).
        """
    )

st.divider()

# --- Section 1: Exercice cardinalités -------------------------------------
st.header("🧩 Exercice 1 – Choisir les cardinalités (MCD)")
left, right = st.columns([1,1])
with left:
    st.markdown("**Consigne :** Pour chaque relation, choisissez la cardinalité la plus adaptée.")

relations = {
    "Membre – Emprunt": "?",
    "Livre – Emprunt": "?",
    "Livre – Catégorie": "?",
}

# Default selections stored in session
if "card_answers" not in st.session_state:
    st.session_state.card_answers = {
        "Membre – Emprunt": CARD_OPTIONS[1],  # 1–N par défaut
        "Livre – Emprunt": CARD_OPTIONS[1],
        "Livre – Catégorie": CARD_OPTIONS[3],
    }

with right:
    for rel in relations:
        st.session_state.card_answers[rel] = st.radio(
            f"Cardinalité pour **{rel}**:",
            CARD_OPTIONS,
            index=CARD_OPTIONS.index(st.session_state.card_answers[rel]),
            horizontal=True,
            key=f"radio_{rel}",
        )

solution_cards = {
    "Membre – Emprunt": "1–N",    # un membre a plusieurs emprunts
    "Livre – Emprunt": "1–N",      # un livre peut générer plusieurs emprunts (dans le temps)
    "Livre – Catégorie": "N–N",    # n catégories pour n livres
}

c_ok = score_cardinality(st.session_state.card_answers, solution_cards)

col1, col2 = st.columns([1,1])
with col1:
    st.success(f"Score cardinalités : **{c_ok}/{len(solution_cards)}** ({pct(c_ok, len(solution_cards))}% correct)")
with col2:
    if st.button("💡 Afficher l'explication", use_container_width=True):
        st.info(
            """
            **Pourquoi 1–N entre Livre et Emprunt ?** Un même *exemplaire physique* de Livre peut être emprunté 
            plusieurs fois **dans le temps** (ex : janvier puis mars), mais pas **simultanément**. 
            Cette règle d'exclusivité temporelle n'apparaît pas dans la cardinalité du MCD ; 
            elle s'applique au niveau métier/contraintes (app, trigger, ou contrôle).
            """
        )

st.divider()

# --- Section 2: Diagramme attendu (Graphviz) ------------------------------
st.header("📈 Schéma conceptuel attendu (MCD)")

dot = r"""
 digraph G {
   graph [rankdir=LR, fontsize=10];
   node [shape=record, fontname="Helvetica"];

   Membre [label="{Membre|id; nom; email; téléphone; date_inscription}"];
   Livre  [label="{Livre|id; titre; auteur; isbn; année; emplacement}"];
   Cat    [label="{Catégorie|id; nom; description}"];
   Emprunt [label="{Emprunt|id; date_emprunt; date_retour_prevue; date_retour; amende}"];

   Membre -> Emprunt [label="1..N", arrowhead=none];
   Livre  -> Emprunt [label="1..N", arrowhead=none];
   Livre  -> Cat     [label="N..N", arrowhead=none];
 }
"""

st.graphviz_chart(dot, use_container_width=True)

st.divider()

# --- Section 3: Quiz Débutant ---------------------------------------------
# (les quiz et logique restent inchangés)
# ... [reste du code identique à la version précédente] ...
