from jarvis.config import POSTGRES_CONFIG
import psycopg2, psycopg2.extras, random

def get_rand_id_subject():
    # Start the connection
    conn = psycopg2.connect(
        **POSTGRES_CONFIG,
        cursor_factory=psycopg2.extras.RealDictCursor
    )    
    cur = conn.cursor()

    # Create and exec the query
    query = "SELECT COUNT(*) FROM subjects;"
    cur.execute(query)
    response = cur.fetchone()

    # Close the connection
    cur.close()
    conn.close()

    # Get a random subject of math
    id_subject = random.randint(1,response['count'])

    return id_subject

def get_subject(subject_id):
    """
    This function will be used to get a subject in the database 
    based on the subject_id
    """
    # Start the connection
    conn = psycopg2.connect(
        **POSTGRES_CONFIG,
        cursor_factory=psycopg2.extras.RealDictCursor
    )    
    cur = conn.cursor()

    # Create and exec the query
    query = f"SELECT * FROM concepts WHERE subject_id = %s"
    cur.execute(query, (subject_id,))
    response = cur.fetchone()

    # Close the connection
    cur.close()
    conn.close()
    
    return dict(response) if response else None

def get_concept(subject_id):
    """
    This function will be used to get a concept in the database 
    based on the subject_id
    """
    # Start the connection
    conn = psycopg2.connect(
        **POSTGRES_CONFIG,
        cursor_factory=psycopg2.extras.RealDictCursor
    )    
    cur = conn.cursor()

    # Create and exec the query
    query = f"SELECT * FROM concepts WHERE subject_id = %s ORDER BY RAND"
    cur.execute(query, (subject_id,))
    response = cur.fetchone()

    # Close the connection
    cur.close()
    conn.close()
    
    return dict(response) if response else None

def save_exercise(
        concept_id,  question,  expected_answer,
        explanation, difficulty, generated_by,model_name):
    """
        This function will be used to get a concept in the database 
        based on the subject_id
    """
    # Start the connection
    conn = psycopg2.connect(
        **POSTGRES_CONFIG,
        cursor_factory=psycopg2.extras.RealDictCursor
    )    
    cur = conn.cursor()

    # Create and exec the query
    query ="""
    INSERT INTO exercises (
        concept_id,
        question,
        expected_answer,
        explanation,
        difficulty,
        generated_by,
        model_name
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    try:
        cur.execute(
            query, 
                (
                    concept_id,
                    question,
                    expected_answer,
                    explanation,
                    difficulty,
                    generated_by,
                    model_name
                )
        )
        conn.commit()
    except Exception as error:
        conn.rollback()
        print(f"Error in database: {error}")
        return None

    finally:
        cur.close()
        conn.close()