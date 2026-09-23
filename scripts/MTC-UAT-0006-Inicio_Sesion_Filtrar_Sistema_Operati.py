import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(viewport={"width":1920,"height":1080})
    page = context.new_page()
    page.goto("http://187.188.104.47:11000/")
    page.get_by_role("textbox", name="Usuario").click()
    page.get_by_role("textbox", name="Usuario").fill("alexander.leal@itw.mx")
    page.get_by_role("textbox", name="Usuario").press("Tab")
    page.get_by_role("textbox", name="Contraseña").click()
    page.get_by_role("textbox", name="Contraseña").fill("sr-40G6gT")
    page.get_by_role("button", name="Iniciar Sesión").click()
    page.get_by_role("button", name="Mis Dispositivos").click()
    page.get_by_role("link", name="Dispositivos Móviles").click()
    page.get_by_role("tab", name="Android").click()
    page.get_by_role("tab", name="iOS").click()
    page.get_by_role("tab", name="Todos").click()
    page.get_by_role("button", name="A alexander.leal").click()
    page.get_by_role("button", name="Cerrar Sesión").click()
    page.get_by_role("button", name="Cerrar Sesión").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
