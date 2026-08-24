import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "CyberDesk Tools"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Утилита 1: Генератор паролей ---
    pass_output = ft.TextField(label="Сгенерированный пароль", read_only=True, width=300)
    
    def generate_password(e):
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        pwd = "".join(random.choice(chars) for _ in range(12))
        pass_output.value = pwd
        page.update()

    pass_btn = ft.ElevatedButton("⚡ Сгенерировать пароль", on_click=generate_password)

    # --- Утилита 2: Веб-клиент ---
    url_input = ft.TextField(label="Введите URL", value="https://google.com", width=300)
    
    def open_link(e):
        target_url = url_input.value.strip()
        if not target_url.startswith("http"):
            target_url = "https://" + target_url
        page.launch_url(target_url)

    web_btn = ft.ElevatedButton("🌐 Открыть в браузере", on_click=open_link)

    # --- Экран 1: Утилиты ---
    view_tools = ft.Column(
        controls=[
            ft.Text("⚡ CyberDesk Dashboard", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_ACCENT),
            ft.Divider(),
            ft.Text("Генератор безопасных паролей:", size=14),
            pass_output,
            pass_btn,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    # --- Экран 2: Браузер ---
    view_browser = ft.Column(
        controls=[
            ft.Text("🌐 Веб-Переходник", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_ACCENT),
            ft.Divider(),
            ft.Text("Введите адрес для быстрого перехода:"),
            url_input,
            web_btn,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    # Контейнер для смены контента
    content_area = ft.Container(content=view_tools, padding=10, expand=True)

    # Логика переключения экранов через нижнее меню
    def on_nav_change(e):
        if e.control.selected_index == 0:
            content_area.content = view_tools
        elif e.control.selected_index == 1:
            content_area.content = view_browser
        page.update()

    # Нижняя навигация (вместо кривых вкладок)
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.DASHBOARD, label="Утилиты"),
            ft.NavigationBarDestination(icon=ft.Icons.LANGUAGE, label="Браузер"),
        ],
    )

    page.add(content_area)

ft.app(target=main)
