project = 'App-API'
copyright = 'ZEIT ONLINE'

source_suffix = '.rst'
master_doc = 'index'

html_theme = "sphinx_zon_theme"
html_theme_options = {
    'editme_link': (
        'https://github.com/ZeitOnline/docs-app-api/edit/master/{page}')
}
html_last_updated_fmt = '%b %d, %Y'
html_extra_path = ['api.yaml', 'swagger.html']
html_static_path = ['node_modules/swagger-ui-dist']
