

# Culturize Docker configuration ( under construction )

1. Install Docker. 
Choose the right version for your system https://docs.docker.com/install/ 

2. Install Docker compose https://docs.docker.com/compose/install/ 
 
3. clone this repository 'git clone https://github.com/PACKED-vzw/CultURIze-Back-End-Docker' on your web-server. And enter the "Culturize-Back-End-Docker" directory.

4.Run the `docker-compose build` to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`

6. Configure your Apache/Nginx to redirect a webhook url to the localhost:8000

For Nginx:
Make a new configuration file in `/etc/nginx/conf.d/` and name it culturize.conf with these contents

```
server {
    listen 80;
    listen [::]:80;

        location /github/ {
                proxy_pass http://127.0.0.1:8000/;}
        } 
```          


Apache2 Example:
<VirtualHost example.com:80>
    ProxyPreserveHost On
    ProxyRequests Off
    ServerName www.example.com
    ServerAlias example.com
    ProxyPass /my-webhook http://127.0.0.1:8000
    ProxyPassReverse /my-webhook http://127.0.0.1:8000
</VirtualHost>

This needs to be added in the apache2 configuration file at  '/etc/apache2/apache2.conf' 

5. Add a webhook to github towards the "http://www.example.com/my-webhook"
https://www.youtube.com/watch?v=S9cjO6V7EXg

toevoegen van ip adres content type veranderen naar json

(Uitleg toevoegen)
6. Add the domain for which you want to culture redirect to happen to Apache/Nginx
<VirtualHost redirectdomain.com:80>
    ProxyPreserveHost On
    ProxyRequests Off
    ServerName www.redirectdomain.com
    ServerAlias redirectdomain.com
    ProxyPass / http://127.0.0.1:8080
    ProxyPassReverse / http://127.0.0.1:8080
</VirtualHost>


Remove the configuration: 
1.
2.
3.
