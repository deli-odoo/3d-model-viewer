from odoo import http
from odoo.http import request

from odoo.addons.sale.controllers.variant import VariantController


class WebsiteSale3DVariantController(VariantController):
    
    @http.route(['/sale/get_combination_info_website'], type='json', auth="public", methods=['POST'], website=True)
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        """Special route to use website logic in get_combination_info override.
        This route is called in JS by appending _website to the base route.
        """
        kw.pop('pricelist_id')
        combination = self.get_combination_info(product_template_id, product_id, combination, add_qty, request.website.get_current_pricelist(), **kw)

        if request.website.google_analytics_key:
            combination['product_tracking_info'] = request.env['product.template'].get_google_analytics_data(combination)

        if request.website.product_page_image_width != 'none' and not request.env.context.get('website_sale_no_images', False):
            product = request.env['product.template'].browse(combination['product_template_id'])
            uploaded = product.file_name
            download_url = '/web/content/%s/%s/model_viewer/%s' % (product._name, product.id, product.file_name) + '?download=true'
            carousel_view = request.env['ir.ui.view']._render_template('website_sale.shop_product_images', values={
                'product': product,
                'product_variant': request.env['product.product'].browse(combination['product_id']),
                'website': request.env['website'].get_current_website(),
                'download_url': download_url,
                'uploaded': uploaded,
            })
            combination['carousel'] = carousel_view
        return combination
    
    @http.route(auth="public")
    def create_product_variant(self, product_template_id, product_template_attribute_value_ids, **kwargs):
        """Override because on the website the public user must access it."""
        return super(WebsiteSale3DVariantController, self).create_product_variant(product_template_id, product_template_attribute_value_ids, **kwargs)
