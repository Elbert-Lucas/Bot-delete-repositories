from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

"""
Esta função automatiza a tarefa de excluir multiplos repositorios do GitHub
ATENÇÃO: cuidado para não excluir repositorios sem querer!!    
"""


def delete(username, password, exception):
    print("#" * 8)
    # Inicialização do selenium:

    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get('https://github.com/login')

    # Login:

    input_username = browser.find_element(By.ID, "login_field")

    input_password = browser.find_element(By.ID, "password")

    enter_input = browser.find_element(By.CSS_SELECTOR,
                                       'body.logged-out.env-production.page-responsive.session-authentication:nth-child(2) div.application-main:nth-child(4) div.auth-form.px-3 div.auth-form-body.mt-3:nth-child(5) form:nth-child(1) div.position-relative:nth-child(4) > input.btn.btn-primary.btn-block.js-sign-in-button:nth-child(13)')

    try:
        input_username.send_keys(username)
        input_password.send_keys(password)
        enter_input.click()

    except:
        print("Usuario ou senha esta errado")
    else:
        # Entra na aba dos repositorios:
        name = browser.find_element(By.CSS_SELECTOR,
                                    'body.logged-in.env-production.page-responsive.full-width:nth-child(2) div.position-relative.js-header-wrapper:nth-child(1) header.Header.js-details-container.Details.px-3.px-md-4.px-lg-5.flex-wrap.flex-md-nowrap:nth-child(4) div.Header-item.position-relative.mr-0.d-none.d-md-flex:nth-child(7) details.details-overlay.details-reset.js-feature-preview-indicator-container summary.Header-link > img.avatar.avatar-small.circle')
        name = name.get_attribute('alt')[1:]

        browser.get(f"https://github.com/{name}?tab=repositories")

        projects = browser.find_element(By.XPATH,
                                        '//body/div[6]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/ul[1]')
        projects = projects.find_elements(By.TAG_NAME,
                                          'li')

        links_projects = []

        # Guarda os links dos repositorios:
        for project in projects:
            nome = project.find_element(By.TAG_NAME, 'a')

            if exception.__contains__(nome.text):
                continue
            links_projects.append(nome.get_attribute('href'))

        # Automação da exclusão (entra nos repositorios e simula os clicks e inputs):
        for link in links_projects:
            browser.get(link + '/settings')
            browser.find_element(By.XPATH, "//summary[contains(text(),'Delete this repository')]").click()

            secure_key = browser.find_element(By.CSS_SELECTOR,
                                              'body.logged-in.env-production.page-responsive:nth-child(2) div.application-main:nth-child(8) div.clearfix.new-discussion-timeline.container-xl.px-3.px-md-4.px-lg-5 div.repository-content div.Layout.Layout--sidebarPosition-start.Layout--sidebarPosition-flowRow-start div.Layout-main div.Layout-main-centered-md div.container-md div.Box.color-border-danger:nth-child(17) li.Box-row.d-flex.flex-items-center:nth-child(4) details.details-reset.details-overlay.details-overlay-dark.flex-md-order-1.flex-order-2 details-dialog.Box.Box--overlay.d-flex.flex-column.anim-fade-in.fast div.Box-body.overflow-auto p:nth-child(2) > strong:nth-child(1)') \
                .text
            input_secure_key = browser.find_element(By.CSS_SELECTOR,
                                                    'body.logged-in.env-production.page-responsive:nth-child(2) div.application-main:nth-child(8) div.clearfix.new-discussion-timeline.container-xl.px-3.px-md-4.px-lg-5 div.repository-content div.Layout.Layout--sidebarPosition-start.Layout--sidebarPosition-flowRow-start div.Layout-main div.Layout-main-centered-md div.container-md div.Box.color-border-danger:nth-child(17) li.Box-row.d-flex.flex-items-center:nth-child(4) details.details-reset.details-overlay.details-overlay-dark.flex-md-order-1.flex-order-2 details-dialog.Box.Box--overlay.d-flex.flex-column.anim-fade-in.fast div.Box-body.overflow-auto form:nth-child(3) p:nth-child(3) > input.form-control.input-block')
            input_secure_key.send_keys(secure_key)

            browser.find_element(By.CSS_SELECTOR,
                                 'body.logged-in.env-production.page-responsive:nth-child(2) div.application-main:nth-child(8) div.clearfix.new-discussion-timeline.container-xl.px-3.px-md-4.px-lg-5 div.repository-content div.Layout.Layout--sidebarPosition-start.Layout--sidebarPosition-flowRow-start div.Layout-main div.Layout-main-centered-md div.container-md div.Box.color-border-danger:nth-child(17) li.Box-row.d-flex.flex-items-center:nth-child(4) details.details-reset.details-overlay.details-overlay-dark.flex-md-order-1.flex-order-2 details-dialog.Box.Box--overlay.d-flex.flex-column.anim-fade-in.fast div.Box-body.overflow-auto form:nth-child(3) > button.btn-danger.btn.btn-block:nth-child(4)') \
                .click()

            print(f'{secure_key} excluido')
