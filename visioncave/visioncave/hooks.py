app_name = "visioncave"
app_title = "VisionCave"
app_publisher = "Your Name"
app_description = "A Frappe app for Computer Vision tasks with n8n and Node-RED integration."
app_email = "your.email@example.com"
app_license = "MIT"

# ... (rest of the hooks.py content remains the same)

# Add settings for n8n and Node-RED integration
# These settings would be accessible through the Frappe app's settings page.
visioncave_settings = {
    "n8n_webhook_url": "",  # URL for receiving webhooks from n8n
    "nodered_broker_url": "",  # URL for connecting to a Node-RED MQTT broker (or other communication method)
    "api_key": "" # API key for authentication
}
