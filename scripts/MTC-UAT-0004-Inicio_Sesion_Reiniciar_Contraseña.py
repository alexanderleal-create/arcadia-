import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(viewport={"width":1920,"height":1080})
    page = context.new_page()
    page.goto("http://187.188.104.47:11000/")
    page.get_by_role("button", name="Reiniciar Contraseña").click()
    page.locator("#formResetUsername").click()
    page.locator("#formResetUsername").fill("alexander.leal@itw.mx")
    page.get_by_role("textbox", name="Correo electrónico registrado").click()
    page.get_by_role("textbox", name="Correo electrónico registrado").fill("alexander.leal@itw.mx")
    page.get_by_role("button", name="Reiniciar", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
