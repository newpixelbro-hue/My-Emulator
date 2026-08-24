import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "CyberDesk Tools"
    page.theme_mode = "dark"
    page.padding = 20
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

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
            ft.Text("⚡ CyberDesk Dashboard", size=22, weight="bold", color="cyanAccent"),
            ft.Divider(),
            ft.Text("Генератор безопасных паролей:", size=14),
            pass_output,
            pass_btn,
        ],
        alignment="start",
        horizontal_alignment="center",
        spacing=15,
    )

    # --- Вкладка 2: Браузер-клиент ---
    tab_browser = ft.Column(
        [
            ft.Text("🌐 Веб-Переходник", size=22, weight="bold", color="cyanAccent"),
            ft.Divider(),
            ft.Text("Введите адрес для быстрого перехода:"),
            url_input,
            web_btn,
        ],
        alignment="start",
        horizontal_alignment="center",
        spacing=15,
    )

    # Навигационные вкладки
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[
            ft.Tab(
                text="Утилиты",
                icon="dashboard",
                content=ft.Container(content=tab_tools, padding=10)
            ),
            ft.Tab(
                text="Браузер",
                icon="language",
                content=ft.Container(content=tab_browser, padding=10)
            ),
        ],
    )

    page.add(tabs)

ft.app(target=main)
