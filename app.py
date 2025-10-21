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

        # Return as plain text
        from flask import Response
        return Response(rendered_config, mimetype='text/plain')
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500