{
    "name": "3D Model Viewer Widget",
    "summary": "3D Model Viewer Widget",
    "description": """
    """,
    "version": "1.0",
    "category": "",
    "license": "OPL-1",
    "depends": ["mrp", "mrp_plm", "website_sale"],
    "data": [
        "views/product_template_inherit.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/3d-model-viewer/static/lib/fullscreen-polyfill.js",
            "/3d-model-viewer/static/src/js/assets.js",
            "/3d-model-viewer/static/src/js/web_widget_model_viewer.xml",
            "/3d-model-viewer/static/src/js/web_widget_model_viewer.js",
        ]
    },
    "demo": [],
    "author": "Odoo Inc",
    "website": "www.odoo.com",
    "application": True,
}
