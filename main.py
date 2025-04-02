from website import create_app
import socket
import os

# Check if we are running in a local environment or production (Vercel)
is_local = os.getenv('FLASK_ENV') == 'development'

if is_local:
    # Get the local IP if running in a local environment
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Your local IP: {local_ip}")
else:
    # For production (Vercel), we will use the default Vercel configuration
    local_ip = "localhost"

app = create_app()

if __name__ == '__main__':
    if is_local:
        print(f"Access the app at: http://{local_ip}:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("App is running on Vercel!")
        app.run(debug=True)
