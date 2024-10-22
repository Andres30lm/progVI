import flet as ft

def main(page):
    tasks = []
    selected_index = None  # Variable para rastrear el índice seleccionado

    def add_clicked(e):
        if new_task.value:
            tasks.append(new_task.value)
            update_task_list()
            new_task.value = ""
            new_task.focus()
            new_task.update()

    def modify_clicked(e):
        if selected_index is not None and new_task.value:
            tasks[selected_index] = new_task.value
            update_task_list()
            new_task.value = ""
            new_task.focus()
            new_task.update()

    def delete_clicked(e):
        nonlocal selected_index  # Usar la variable externa
        if selected_index is not None:
            tasks.pop(selected_index)  # Eliminar la tarea seleccionada
            selected_index = None  # Reiniciar el índice seleccionado
            update_task_list()
            new_task.value = ""  # Limpiar el campo de texto después de eliminar
            new_task.update()

    def update_task_list():
        task_list.controls.clear()
        for i, task in enumerate(tasks):
            checkbox = ft.Checkbox(label=task, value=False)
            checkbox.on_change = lambda e, index=i: task_list_select(index)
            task_list.controls.append(checkbox)
        task_list.update()

    def task_list_select(index):
        nonlocal selected_index  # Usar la variable externa
        selected_index = index  # Actualizar el índice seleccionado
        new_task.value = tasks[selected_index]  # Llenar el campo de texto con la tarea seleccionada
        new_task.update()

    new_task = ft.TextField(hint_text="Realice su pedido", width=300)

    logo = ft.Image(src="img/cafe1.jpg", width=150, height=150)
    header_text = ft.Text("BIENVENIDOS A LA CAFETERIA", size=20, weight=ft.FontWeight.BOLD)
    header = ft.Column(
        controls=[logo, header_text],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los elementos del encabezado
        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alineación horizontal centrada
    )

    task_list = ft.Column()  # Para listar las tareas

    page.add(
        ft.Column(
            controls=[
                header,
                ft.Divider(height=20),
                ft.Row(
                    controls=[new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)],
                    alignment=ft.MainAxisAlignment.CENTER  # Centrar la fila del campo de texto y botón
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Modificar", on_click=modify_clicked),
                        ft.ElevatedButton("Eliminar", on_click=delete_clicked)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centrar la fila de botones
                ),
                task_list
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar la columna principal
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alineación horizontal centrada
        )
    )

    # Establecer tamaño de la página
    page.window_width = 600
    page.window_height = 400
    page.update()

ft.app(main)