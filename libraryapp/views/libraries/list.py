import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def library_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.libraryId,
            l.library_name,
            l.library_address,
        from libraryapp_library l
        """)

        all_libraries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            library = Library()
            library.id = row["id"]
            library.name = row["name"]
            library.address = row["address"]

            all_libraries.append(lib)

    template_name = 'library/list.html'

    context = {
        'all_libraries': all_libraries
    }

    return render(request, template_name, context)