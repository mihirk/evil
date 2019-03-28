wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip
unzip ngrok-stable-linux-386.zip
chmod a+x ngrok
python -m SimpleHTTPServer 8080&
./ngrok 8080
