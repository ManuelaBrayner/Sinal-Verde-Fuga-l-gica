def implica(a, b):
    """Condicional a → b."""
    return (not a) or b


def criar(nivel, enunciado, correta, erradas, explicacao):
    """Monta o dicionário de uma questão.
    enunciado e correta: tupla (texto, função).
    erradas: lista de tuplas (texto, função)."""
    funcao, n_vars = enunciado[1], enunciado[1].__code__.co_argcount
    return {
        'nivel': nivel,
        'enunciado': enunciado[0],
        'correta': correta[0],
        'erradas': [e[0] for e in erradas],
        'explicacao': explicacao,
        # Campos usados só pelo validador:
        'n_vars': n_vars,
        'f_enunciado': funcao,
        'f_correta': correta[1],
        'f_erradas': [e[1] for e in erradas],
    }


QUESTOES = [
    # ---------------- NÍVEL 1 ----------------
    criar(1,
          ('¬(P ∧ Q)', lambda p, q: not (p and q)),
          ('¬P ∨ ¬Q', lambda p, q: (not p) or (not q)),
          [('¬P ∧ ¬Q', lambda p, q: (not p) and (not q)),
           ('P ∨ Q', lambda p, q: p or q),
           ('P ∧ ¬Q', lambda p, q: p and (not q))],
          'De Morgan: a negação da conjunção vira disjunção das negações.'),

    criar(1,
          ('¬(P ∨ Q)', lambda p, q: not (p or q)),
          ('¬P ∧ ¬Q', lambda p, q: (not p) and (not q)),
          [('¬P ∨ ¬Q', lambda p, q: (not p) or (not q)),
           ('P ∧ Q', lambda p, q: p and q),
           ('¬P ∨ Q', lambda p, q: (not p) or q)],
          'De Morgan: a negação da disjunção vira conjunção das negações.'),

    criar(1,
          ('¬¬P', lambda p: not (not p)),
          ('P', lambda p: p),
          [('¬P', lambda p: not p),
           ('P ∧ ¬P', lambda p: p and (not p)),
           ('P ∨ ¬P', lambda p: p or (not p))],
          'Dupla negação: negar duas vezes devolve a proposição original.'),

    criar(1,
          ('P → Q', lambda p, q: implica(p, q)),
          ('¬P ∨ Q', lambda p, q: (not p) or q),
          [('P ∨ ¬Q', lambda p, q: p or (not q)),
           ('¬P ∧ Q', lambda p, q: (not p) and q),
           ('P ∧ ¬Q', lambda p, q: p and (not q))],
          'Condicional como disjunção: P → Q só é falsa quando P é V e Q é F.'),

    # ---------------- NÍVEL 2 ----------------
    criar(2,
          ('P → Q', lambda p, q: implica(p, q)),
          ('¬Q → ¬P', lambda p, q: implica(not q, not p)),
          [('Q → P', lambda p, q: implica(q, p)),
           ('¬P → ¬Q', lambda p, q: implica(not p, not q)),
           ('P → ¬Q', lambda p, q: implica(p, not q))],
          'Contrapositiva: P → Q equivale a ¬Q → ¬P. (Q → P é a recíproca; ¬P → ¬Q é a inversa.)'),

    criar(2,
          ('¬(P → Q)', lambda p, q: not implica(p, q)),
          ('P ∧ ¬Q', lambda p, q: p and (not q)),
          [('¬P → ¬Q', lambda p, q: implica(not p, not q)),
           ('¬P ∧ Q', lambda p, q: (not p) and q),
           ('P → ¬Q', lambda p, q: implica(p, not q))],
          'Negação da condicional: só é verdadeira quando P é V e Q é F.'),

    criar(2,
          ('P ∨ (P ∧ Q)', lambda p, q: p or (p and q)),
          ('P', lambda p, q: p),
          [('Q', lambda p, q: q),
           ('P ∧ Q', lambda p, q: p and q),
           ('P ∨ Q', lambda p, q: p or q)],
          'Absorção: P ∨ (P ∧ Q) ≡ P.'),

    criar(2,
          ('P ∧ (P ∨ Q)', lambda p, q: p and (p or q)),
          ('P', lambda p, q: p),
          [('P ∨ Q', lambda p, q: p or q),
           ('Q', lambda p, q: q),
           ('P ∧ Q', lambda p, q: p and q)],
          'Absorção: P ∧ (P ∨ Q) ≡ P.'),

    # ---------------- NÍVEL 3 ----------------
    criar(3,
          ('P ↔ Q', lambda p, q: p == q),
          ('(P → Q) ∧ (Q → P)', lambda p, q: implica(p, q) and implica(q, p)),
          [('(P → Q) ∨ (Q → P)', lambda p, q: implica(p, q) or implica(q, p)),
           ('P ∧ Q', lambda p, q: p and q),
           ('P → Q', lambda p, q: implica(p, q))],
          'Bicondicional: P ↔ Q equivale às duas condicionais ao mesmo tempo.'),

    criar(3,
          ('P → (Q → R)', lambda p, q, r: implica(p, implica(q, r))),
          ('(P ∧ Q) → R', lambda p, q, r: implica(p and q, r)),
          [('(P → Q) → R', lambda p, q, r: implica(implica(p, q), r)),
           ('(P ∨ Q) → R', lambda p, q, r: implica(p or q, r)),
           ('P → (Q ∧ R)', lambda p, q, r: implica(p, q and r))],
          'Exportação: P → (Q → R) equivale a (P ∧ Q) → R.'),

    criar(3,
          ('¬(P ↔ Q)', lambda p, q: p != q),
          ('(P ∧ ¬Q) ∨ (¬P ∧ Q)', lambda p, q: (p and not q) or ((not p) and q)),
          [('¬P ↔ ¬Q', lambda p, q: (not p) == (not q)),
           ('(P ∧ Q) ∨ (¬P ∧ ¬Q)', lambda p, q: (p and q) or ((not p) and (not q))),
           ('¬P ∧ ¬Q', lambda p, q: (not p) and (not q))],
          'Negação da bicondicional: P e Q têm valores diferentes (ou exclusivo).'),

    criar(3,
          ('P → (Q ∧ R)', lambda p, q, r: implica(p, q and r)),
          ('(P → Q) ∧ (P → R)', lambda p, q, r: implica(p, q) and implica(p, r)),
          [('(P → Q) ∨ (P → R)', lambda p, q, r: implica(p, q) or implica(p, r)),
           ('(P ∧ Q) → R', lambda p, q, r: implica(p and q, r)),
           ('P → (Q ∨ R)', lambda p, q, r: implica(p, q or r))],
          'Distributividade: P → (Q ∧ R) equivale a (P → Q) ∧ (P → R).'),
]

