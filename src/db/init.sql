CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    discord_id VARCHAR(50) UNIQUE,
    username VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);


CREATE TABLE concepts (
    id SERIAL PRIMARY KEY,

    subject_id INTEGER NOT NULL
        REFERENCES subjects(id)
        ON DELETE CASCADE,

    name VARCHAR(100) NOT NULL,
    description TEXT,

    UNIQUE(subject_id, name)
);


CREATE TABLE exercises (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    concept_id INTEGER
        REFERENCES concepts(id)
        ON DELETE SET NULL,

    question TEXT NOT NULL,
    expected_answer TEXT,
    explanation TEXT,

    difficulty INTEGER
        CHECK (difficulty BETWEEN 1 AND 5),

    generated_by VARCHAR(50) DEFAULT 'mistral',
    model_name VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    user_id INTEGER NOT NULL
        REFERENCES users(id)
        ON DELETE CASCADE,

    exercise_id UUID NOT NULL
        REFERENCES exercises(id)
        ON DELETE CASCADE,

    answer TEXT NOT NULL,

    is_correct BOOLEAN NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO subjects (name, description)
VALUES
    ('Ensembles', 'Ensembles, opérations et relations'),
    ('Logique', 'Propositions, raisonnements et logique'),
    ('Algèbre de Boole', 'Variables et opérations booléennes'),
    ('Arithmétique', 'Entiers, divisibilité et propriétés arithmétiques'),
    ('Calcul matriciel', 'Matrices et opérations matricielles'),
    ('Théorie des graphes', 'Graphes, parcours et algorithmes'),
    ('Nombres complexes', 'Calcul et représentation des nombres complexes'),
    ('Séries de Fourier', 'Décomposition de fonctions périodiques');

INSERT INTO concepts (subject_id, name, description)
VALUES

-- Ensembles
(1, 'Opérations sur les ensembles',
 'Union, intersection, différence et complémentaire'),

(1, 'Relations',
 'Relations entre éléments et ensembles'),

-- Logique
(2, 'Propositions logiques',
 'Propositions et valeurs de vérité'),

(2, 'Tables de vérité',
 'Construction et analyse de tables de vérité'),

-- Algèbre de Boole
(3, 'Opérations booléennes',
 'AND, OR, NOT et opérations dérivées'),

(3, 'Simplification booléenne',
 'Simplification des expressions booléennes'),

-- Arithmétique
(4, 'PGCD',
 'Plus grand commun diviseur'),

(4, 'PPCM',
 'Plus petit commun multiple'),

(4, 'Nombres premiers',
 'Propriétés et décomposition en facteurs premiers'),

-- Calcul matriciel
(5, 'Opérations sur les matrices',
 'Addition, multiplication et transposée'),

(5, 'Déterminants',
 'Calcul et propriétés des déterminants'),

-- Théorie des graphes
(6, 'Graphes',
 'Sommets, arêtes et représentations'),

(6, 'Parcours de graphes',
 'Parcours en largeur et en profondeur'),

-- Nombres complexes
(7, 'Forme algébrique',
 'Partie réelle et partie imaginaire'),

(7, 'Forme exponentielle',
 'Représentation exponentielle des complexes'),

-- Séries de Fourier
(8, 'Fonctions périodiques',
 'Propriétés des fonctions périodiques'),

(8, 'Décomposition de Fourier',
 'Coefficients et séries de Fourier');

INSERT INTO users (discord_id, username)
VALUES ('development-user', 'Sulyvan');