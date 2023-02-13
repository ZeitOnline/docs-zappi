project = 'Zappi (App-API)'
copyright = 'ZEIT ONLINE'

source_suffix = '.rst'
master_doc = 'index'

html_theme = "zondocs_theme"
html_theme_options = {
    'editme_link': (
        'https://github.com/ZeitOnline/docs-zappi/edit/master/{page}')
}
html_last_updated_fmt = '%b %d, %Y'
html_extra_path = ['api/api.yaml', 'api/swagger.html']
html_static_path = ['api/node_modules/swagger-ui-dist']
