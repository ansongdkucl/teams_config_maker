#!/usr/bin/env python3
from flask import Flask, request, jsonify
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

# Setup Jinja2 environment to look inside the 'templates' folder
env = Environment(loader=FileSystemLoader('templates'))

@app.route('/generate', methods=['POST'])
def generate_config():
    try:
        data = request.json
        hostname = data.get('hostname')
        vlan = data.get('vlan')
        interface = data.get('interface')
        description = data.get('description', 'Access Port')

        # Load the template
        template = env.get_template('switch_template.txt')

        # Render the config with variables
        rendered_config = template.render(
            hostname=hostname,
            vlan=vlan,
            interface=interface,
            description=description
        )

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
    app.run(port=5002)
