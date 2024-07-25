import subprocess
import time
import socket

# Function to start the Minecraft server
def start_server():
    server_jar = "minecraft_server.jar"  # Path to your Minecraft server JAR file
    subprocess.Popen(["java", "-Xmx1024M", "-Xms1024M", "-jar", server_jar, "nogui"])

# Function to check if the server is listening on port 25565
def check_server():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect(("localhost", 25565))
                print("Minecraft server is running and listening on port 25565")
                break
            except ConnectionRefusedError:
                print("Minecraft server is not yet running. Retrying in 5 seconds...")
                time.sleep(5)

if __name__ == "__main__":
    # Start the Minecraft server
    start_server()

    # Check if the server is running and listening on port 25565
    check_server()

    # Now you can connect to the Minecraft server using the Minecraft client
