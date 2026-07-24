from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)



@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM users
            WHERE username=%s AND password=%s
            """,
            (username, password)
        )

        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            return redirect("/dashboard")

        return render_template(
            "login.html",
            msg="Invalid Username or Password"
        )

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cur = conn.cursor()

        try:
            cur.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (%s, %s, %s)
                """,
                (username, email, password)
            )

            conn.commit()

            cur.close()
            conn.close()

            return redirect("/")

        except Exception:
            conn.rollback()
            cur.close()
            conn.close()

            return render_template(
                "signup.html",
                msg="Username or Email already exists."
            )

    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():

    conn = get_connection()
    cur = conn.cursor()

    # Total Tasks
    cur.execute("SELECT COUNT(*) FROM tasks")
    total = cur.fetchone()[0]

    # Pending Tasks
    cur.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'")
    pending = cur.fetchone()[0]

    # Completed Tasks
    cur.execute("SELECT COUNT(*) FROM tasks WHERE status='Completed'")
    completed = cur.fetchone()[0]

    # Pending task list
    cur.execute("""
        SELECT id, subject, topic, deadline
        FROM tasks
        WHERE status='Pending'
        ORDER BY deadline
    """)
    pending_tasks = cur.fetchall()

    # Completed task list
    cur.execute("""
    SELECT id, subject, topic, deadline
    FROM tasks
    WHERE status='Completed'
    ORDER BY deadline DESC
""")
    completed_tasks = cur.fetchall()

    # Recent Tasks
    cur.execute("""
        SELECT id, subject, topic, deadline, status
        FROM tasks
        ORDER BY id DESC
        LIMIT 10
    """)
    recent_tasks = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        pending=pending,
        completed=completed,
        pending_tasks=pending_tasks,
        completed_tasks=completed_tasks,
        recent_tasks=recent_tasks
    )


@app.route("/add_task", methods=["POST"])
def add_task():

    subject = request.form["subject"]
    topic = request.form["topic"]
    deadline = request.form["deadline"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO tasks(subject, topic, deadline)
        VALUES(%s,%s,%s)
        """,
        (subject, topic, deadline)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/dashboard")


@app.route("/pending")
def pending():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM tasks WHERE status='Pending'"
    )

    tasks = cur.fetchall()
    print(tasks)
    cur.close()
    conn.close()

    return render_template(
        "pending.html",
        tasks=tasks
    )


@app.route("/completed")
def completed():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM tasks WHERE status='Completed'"
    )

    tasks = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "completed.html",
        tasks=tasks
    )


@app.route("/complete/<int:id>")
def complete(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tasks
        SET status='Completed'
        WHERE id=%s
        """,
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/pending")


if __name__ == "__main__":
    app.run(debug=True)
