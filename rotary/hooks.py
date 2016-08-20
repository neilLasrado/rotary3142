# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rotary"
app_title = "Rotary"
app_publisher = "Neil Lasrado"
app_description = "Reporting system for Rotary"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "neil@rotaractsuncity.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rotary/css/rotary.css"
# app_include_js = "/assets/rotary/js/rotary.js"

# include js, css files in header of web template
# web_include_css = "/assets/rotary/css/rotary.css"
# web_include_js = "/assets/rotary/js/rotary.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rotary.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rotary.install.before_install"
# after_install = "rotary.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rotary.notifications.get_notification_config"

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
# 		"rotary.tasks.all"
# 	],
# 	"daily": [
# 		"rotary.tasks.daily"
# 	],
# 	"hourly": [
# 		"rotary.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rotary.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rotary.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rotary.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rotary.event.get_events"
# }

