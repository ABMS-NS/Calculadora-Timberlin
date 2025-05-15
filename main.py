import flet as ft
from funcs import *


def main(page: ft.Page):
    # DEFINIÇÃO DAS FUNÇÕES DE ALTERAÇÃO DOS DROPDOWNS
    def on_classe_change(e):
        nonlocal classe_selecionada
        classe_selecionada = classe_dropdown.value

    def on_origem_change(e):
        nonlocal origem_selecionada
        origem_selecionada = origem_dropdown.value

    def on_suborigem_change(e):
        nonlocal suborigem_selecionada
        suborigem_selecionada = suborigem_dropdown.value

    def on_buff_origem_change(e):
        nonlocal buff_origem_selecionado
        buff_origem_selecionado = buff_origem_dropdown.value

    def calcular_vida(lvl: int, classe, subclasse, vigor: int, firmeza: int, bonus: int):
        return Vida.calcular(lvl, classe, subclasse, vigor, firmeza, bonus)

    def calcular_alma(lvl: int, origem: int, alma: int, bonus: int):
        return Alma.calcular(lvl, origem, alma, bonus)

    def calcular_estamina(lvl: int, classe, subclasse, vigor: int, firmeza: int, medicina: int, bonus: int):
        return Estamina.calcular(lvl, classe, subclasse, vigor, firmeza, medicina, bonus)

    def calcular_espirito(lvl: int, classe, subclasse, origem, suborigem, buff_origem, alma: int, espiritualidade: int, bonus: int):
        return Espirito.calcular(lvl, classe, subclasse, origem, suborigem, buff_origem, alma, espiritualidade, bonus)

    page.title = "Calculadora Timberlin"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # Cores
    quase_preto = "#0D0F11"
    cinza_claro = "#F5F3F5"
    rosa_suave = "#FF70A6"
    cinza_escuro = "#292929"
    escuro_verde_oliva = "#1C1C1C"
    verde_menta = "#A9D8D3"
    red = "#FA6C6C"


    # Título
    titulo = ft.Text("CALCULADORA TIMBERLIN", size=30, font_family="Arial bold", weight="bold", color=cinza_claro)
    creditos = ft.Text("Feito com muito ódio ao excel e amor ao Autumn por Alison", size=10, font_family="Arial", color="#363636")

    # Campos de entrada
    texto = ft.Text("Dados do personagem", size=15, font_family="Arial bold", weight="bold")
    nome = ft.TextField(label="Nome")
    lvl = ft.TextField(label="Lv", width=65, text_align=ft.TextAlign.CENTER)
    alma = ft.TextField(label="Alma", width=86, text_align=ft.TextAlign.CENTER)
    vigor = ft.TextField(label="Vigor", width=86, text_align=ft.TextAlign.CENTER)
    firmeza = ft.TextField(label="Firmeza", width=86, text_align=ft.TextAlign.CENTER)
    medicina = ft.TextField(label="Med.", width=65, text_align=ft.TextAlign.CENTER)
    espiritualidade = ft.TextField(label="Esp.", width=86, text_align=ft.TextAlign.CENTER)
    vida_b = ft.TextField(label="Vida", text_align=ft.TextAlign.CENTER)
    alma_b = ft.TextField(label="Alma", text_align=ft.TextAlign.CENTER)
    estamina_b = ft.TextField(label="Estamina", text_align=ft.TextAlign.CENTER)
    espirito_b = ft.TextField(label="Espirito", text_align=ft.TextAlign.CENTER)

    # Dropdowns
    classe_selecionada = "Nenhuma"
    origem_selecionada = "Nenhuma"
    suborigem_selecionada = "Nenhuma"
    buff_origem_selecionado = "Nenhuma"

    classe_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Nenhuma"),
            ft.dropdown.Option("Desafiante"),
            ft.dropdown.Option("Bastião"),
            ft.dropdown.Option("Equilibrista"),
            ft.dropdown.Option("Socorrista"),
            ft.dropdown.Option("Atirador"),
            ft.dropdown.Option("Amaldiçoado"),
        ],
        label="Classe",
        width=300,
        on_change=on_classe_change,
        value="Nenhuma",
    )

    origem_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Nenhuma"),
            ft.dropdown.Option("Manipulador de alma"),
            ft.dropdown.Option("Aura"),
            ft.dropdown.Option("Espirituoso"),
            ft.dropdown.Option("Artista Astral"),
            ft.dropdown.Option("Mascarado e Contratante"),
            ft.dropdown.Option("Bruxo"),
            ft.dropdown.Option("Retornado"),
        ],
        label="Origem",
        width=300,
        on_change=on_origem_change,
        value="Nenhuma",
    )

    suborigem_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Nenhuma"),
            ft.dropdown.Option("Aura"),
            ft.dropdown.Option("Espirituoso"),
            ft.dropdown.Option("Artista Astral"),
            ft.dropdown.Option("Mascarado e Contratante"),
            ft.dropdown.Option("Bruxo"),
        ],
        label="Sub-origem",
        width=300,
        on_change=on_suborigem_change,
        value="Nenhuma",
    )

    buff_origem_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Nenhuma"),
            ft.dropdown.Option("Manipulador de alma"),
            ft.dropdown.Option("Aura"),
            ft.dropdown.Option("Espirituoso"),
            ft.dropdown.Option("Artista Astral"),
            ft.dropdown.Option("Mascarado e Contratante"),
            ft.dropdown.Option("Bruxo"),
            ft.dropdown.Option("Retornado"),
        ],
        label="Buff de origem",
        width=300,
        on_change=on_buff_origem_change,
        value="Nenhuma",
    )

    subclasse_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Nenhuma"),
            ft.dropdown.Option("Algoz"),
            ft.dropdown.Option("Berserk"),
            ft.dropdown.Option("Duelista"),
            ft.dropdown.Option("Inabalável"),
            ft.dropdown.Option("Etéreo"),
            ft.dropdown.Option("Artesão"),
            ft.dropdown.Option("Xamã"),
        ],
        label="Sub-classe",
        width=300,
        value="Nenhuma",
    )

    entrada = ft.Container(
        content=ft.Column([
            texto,
            ft.Divider(),
            nome,
            origem_dropdown,
            classe_dropdown,
            subclasse_dropdown,
            suborigem_dropdown,
            buff_origem_dropdown,
            ft.Divider(),
            ft.Row([lvl, alma, vigor]),
            ft.Row([medicina, firmeza, espiritualidade]),
        ]),
        border=ft.border.all(1),
        border_radius=10,
        padding=20,
        width=300,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    bonus = ft.Container(
        content=ft.Column([
            ft.Text("Bônus de status", size=15, font_family="Arial bold", weight="bold"),
            ft.Divider(),
            vida_b,
            alma_b,
            estamina_b,
            espirito_b,
        ]),
        border=ft.border.all(1),
        border_radius=10,
        padding=20,
        width=300,
    )

    resultado_texto = ft.Text("", color=cinza_claro)

    def on_calcular_click(e):
        try:
            nivel = int(lvl.value)
            subclasse = subclasse_dropdown.value
            v_vigor = int(vigor.value)
            v_firmeza = int(firmeza.value)
            v_alma = int(alma.value)
            v_medicina = int(medicina.value)
            v_espiritualidade = int(espiritualidade.value)

            b_vida = int(vida_b.value or 0)
            b_alma = int(alma_b.value or 0)
            b_estamina = int(estamina_b.value or 0)
            b_espirito = int(espirito_b.value or 0)

            vida = calcular_vida(nivel, classe_selecionada, subclasse, v_vigor, v_firmeza, b_vida)
            alma_val = calcular_alma(nivel, origem_selecionada, v_alma, b_alma)
            estamina = calcular_estamina(nivel, classe_selecionada, subclasse, v_vigor, v_firmeza, v_medicina, b_estamina)
            espirito = calcular_espirito(nivel, classe_selecionada, subclasse, origem_selecionada, suborigem_selecionada, buff_origem_selecionado, v_alma, v_espiritualidade, b_espirito)

            resultado_texto.value = f"""
⚔️ {nome.value or "Personagem"} (Lv {nivel})

=====================  

Classe: {classe_selecionada} |
Sub-classe: {subclasse} |
Origem: {origem_selecionada} |
Sub-origem: {suborigem_selecionada} |
Buff de origem: {buff_origem_selecionado} |

=====================

❤️ Vida: {vida}
💀 Alma: {alma_val}
⚡ Estamina: {estamina}
✨ Espírito: {espirito}

=====================
"""
        except Exception as err:
            resultado_texto.value = f"Erro: {err}"
        page.update()

    buton = ft.Container(
        content=ft.Column([
            ft.Text("Calcular", size=15, font_family="Arial bold", weight="bold"),
            ft.Divider(),
            ft.ElevatedButton("Calcular", on_click=on_calcular_click),
        ]),
        border=ft.border.all(1),
        border_radius=10,
        padding=20,
        width=300,
    )

    resultado = ft.Container(
    content=ft.Column([
        ft.Text("Resultado", size=15, font_family="Arial bold", weight="bold", color=cinza_claro),
        ft.Divider(),
        ft.Container(
            content=resultado_texto,
            width=300,
            padding=20,
            border=ft.border.all(1, color=verde_menta),
            border_radius=10,
            bgcolor=escuro_verde_oliva,
        ),
    ]),
    border=ft.border.all(1, color=verde_menta),
    border_radius=10,
    padding=20,
    width=300,
)


    page.add(
        ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([
            ft.Column([entrada,], spacing=50),
            ft.Column([bonus, buton,]),
            ft.Column([resultado, creditos]),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=50),
    )


ft.app(target=main)