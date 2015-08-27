FROM richarvey/nginx-php-fpm

RUN rm -f /etc/php5/fpm/php-fpm.conf
ADD config/php-fpm.conf /etc/php5/fpm/php-fpm.conf
RUN rm -f /etc/nginx/nginx.conf
ADD config/nginx.conf /etc/nginx/nginx.conf
ADD getip.sh /root/getip.sh
RUN php5-fpm
RUN nginx -c /etc/nginx/nginx.conf
