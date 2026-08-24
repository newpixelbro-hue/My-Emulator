import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "CyberDesk Tools"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Утилита 1: Генератор паролей ---
    pass_output = ft.TextField(label="Сгенерированный пароль", read_only=True, width=280)
    
    def generate_password(e):
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        pwd = "".join(random.choice(chars) for _ in range(12))
        pass_output.value = pwd
        page.update()

    pass_btn = ft.ElevatedButton("Сгенерировать пароль", on_click=generate_password)

    # --- Утилита 2: Встроенный мини-браузер (Web View) ---
    url_input = ft.TextField(label="Введите URL (например, https://google.com)", value="https://google.com", width=280)
    
    # WebView для отображения сайтов внутри приложения
    web_view = ft.WebView(
        url="https://google.com",
        expand=True,
        on_page_started=lambda e: print("Загрузка..."),
        on_page_ended=lambda e: print("Загружено!"),
    )

    def load_site(e):
        target_url = url_input.value.strip()
        if not target_url.startswith("http"):
            target_url = "https://" + target_url
        web_view.url = target_url
        page.update()

    go_btn = ft.ElevatedButton("Открыть сайт", on_click=load_site)

    # --- Навигация по вкладкам (Главная / Инструменты / Браузер) ---
    
    # Содержимое вкладки "Главная / Утилиты"
    tab_tools = ft.Column(
        [
            ft.Text("⚡ CyberDesk Dashboard", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN_ACCENT),
            ft.Divider(),
            ft.Text("Генератор безопасных паролей:", size=14),
            pass_output,
            pass_btn,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        scroll=ft.ScrollMode.AUTO
    )

    # Содержимое вкладки "Браузер"
    tab_browser = ft.Column(
        [
            ft.Row([url_input, go_btn], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(content=web_view, expand=True, border_radius=10, border=ft.border.all(1, ft.colors.CYAN))
        ],
        expand=True,
        spacing=10
    )

    # Основные вкладки приложения
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[
            ft.Tab(
                text="Утилиты",
                icon=ft.icons.DASHBOARD,
                content=ft.Container(content=tab_tools, padding=10)
            ),
            ft.Tab(
                text="Браузер",
                icon=ft.icons.LANGUAGE,
                content=ft.Container(content=tab_browser, padding=10)
            ),
        ],
    )

    page.add(tabs)

ft.app(target=main)
