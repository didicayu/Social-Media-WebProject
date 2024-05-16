from splinter.browser import Browser

def before_all(context):
    context.created_instances = []
    context.browser = Browser('chrome', headless=True)


def after_all(context):
    context.browser.quit()
    context.browser = None
