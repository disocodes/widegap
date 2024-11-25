from frappe import _
from frappe.utils import get_url

def get_context(context):
    context.cards = [
        {
            "title": _("Residential Vision"),
            "link": get_url("/app/visioncave/residential_vision"), # Replace with actual route
            "icon": "icon-home"
        },
        {
            "title": _("Hospital Vision"),
            "link": get_url("/app/visioncave/hospital_vision"), # Replace with actual route
            "icon": "icon-hospital"
        },
        {
            "title": _("Minesite Vision"),
            "link": get_url("/app/visioncave/minesite_vision"), # Replace with actual route
            "icon": "icon-mine"
        },
        {
            "title": _("School Vision"),
            "link": get_url("/app/visioncave/school_vision"), # Replace with actual route
            "icon": "icon-school"
        },
        {
            "title": _("Traffic Vision"),
            "link": get_url("/app/visioncave/traffic_vision"), # Replace with actual route
            "icon": "icon-traffic"
        },
    ]
