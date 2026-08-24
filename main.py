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

    # --- Утилита 2: Веб-клиент (открытие ссылок) ---
    url_input = ft.TextField(label="Введите URL", value="https://google.com", width=300)
    
    def open_link(e):
        target_url = url_input.value.strip()
        if not target_url.startswith("http"):
            target_url = "https://" + target_url
        page.launch_url(target_url)

    web_btn = ft.ElevatedButton("🌐 Открыть в браузере", on_click=open_link)

    # --- Вкладка 1: Инструменты ---
    tab_tools = ft.Column(
        [
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

    # --- Вкладка 2: Браузер-клиент ---
    tab_browser = ft.Column(
        [
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

    # Навигационные вкладки
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[
            ft.Tab(
                label="Утилиты",
                icon=ft.Icons.DASHBOARD,
                content=ft.Container(content=tab_tools, padding=10)
            ),
            ft.Tab(
                label="Браузер",
                icon=ft.Icons.LANGUAGE,
                content=ft.Container(content=tab_browser, padding=10)
            ),
        ],
    )

    page.add(tabs)

ft.app(target=main)
