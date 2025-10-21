#!/usr/bin/env python3
from flask import Flask, request, jsonify
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

@app.route('/generate', methods=['POST'])
def generate_config():
    try:
        data = request.json
        hostname = data.get('hostname')
        location = data.get('location')
        access_vlan = data.get('access_vlan')
        voice_vlan = data.get('voice_vlan')
        ip_address = data.get('ip_address')

        # Load the template
        template = env.get_template('switch_template.txt')

        # Render the config with variables
        rendered_config = template.render(
            hostname=hostname,
            location=location,
            access_vlan=access_vlan,
            voice_vlan=voice_vlan,
            ip_address=ip_address
        )
        # Ensure proper newlines are preserved
        rendered_config = rendered_config.replace('\r\n', '\n').replace('\r', '\n')


        return jsonify({
            "success": True,
            "config": rendered_config
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/', methods=['GET'])
def index():
    return "✅ Config Generator is running!"

if __name__ == '__main__':
    app.run(port=5000)
