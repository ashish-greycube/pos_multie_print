# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pos_multie_print"
app_title = "POS Multiple Print"
app_publisher = "GreyCube Technologies"
app_description = "App that does multi printing of invoice on different printers"
app_icon = "octicon octicon-versions"
app_color = "orange"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pos_multie_print/css/pos_multie_print.css"
# app_include_js = "/assets/pos_multie_print/js/jsrsasign-all-min.js"

# include js, css files in header of web template
# web_include_css = "/assets/pos_multie_print/css/pos_multie_print.css"
# web_include_js = "/assets/pos_multie_print/js/pos_multie_print.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"ToDo" : "public/js/todo.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pos_multie_print.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pos_multie_print.install.before_install"
# after_install = "pos_multie_print.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pos_multie_print.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pos_multie_print.tasks.all"
# 	],
# 	"daily": [
# 		"pos_multie_print.tasks.daily"
# 	],
# 	"hourly": [
# 		"pos_multie_print.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pos_multie_print.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pos_multie_print.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pos_multie_print.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pos_multie_print.event.get_events"
# }

