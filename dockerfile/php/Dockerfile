FROM richarvey/nginx-php-fpm

RUN rm -f /etc/php5/fpm/php-fpm.conf
ADD config/php-fpm.conf /etc/php5/fpm/php-fpm.conf
RUN rm -f /etc/nginx/nginx.conf
Add config/nginx.conf /etc/nginx/nginx.conf
RUN php5-fpm
RUN nginx

CMD ["/bin/bash"]
