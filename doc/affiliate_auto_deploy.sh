#!/bin/bash

# auto checkout svn
echo "============= start =============="
SVN_SERVER=http://svn.xinggeq.com/svn/xingcloud/MultiLang/Affiliate/trunk/affiliate
SVN_USER=wangkang
SVN_PASSWD=elextech%2012
CHECKOUT_FOLDER="affiliate_"`date +%Y%m%d%H%m%S`
CURRENT_DIR=/home/kratos

echo "Please select online project:"
select AFFILIATE_HOME in "AFFILIATE_HADES" "AFFILIATE_BOSEIDON" "API_HADES" "API_BOSEIDON"; do
   AFFILIATE_HOME=$CURRENT_DIR/srv/$AFFILIATE_HOME/
   break;
done
echo "You have chosen the project: $AFFILIATE_HOME"

cd $CURRENT_DIR/checkout/
mkdir $CHECKOUT_FOLDER

cd $CHECKOUT_FOLDER/
svn checkout $SVN_SERVER --username $SVN_USER --password $SVN_PASSWD

echo "-------------------------------"
echo "Checkout svn code successfully!"
echo "-------------------------------"


# auto cp project
rm -rf $AFFILIATE_HOME/affiliate
cp -r $CURRENT_DIR/checkout/$CHECKOUT_FOLDER/affiliate $AFFILIATE_HOME

echo -e "\n"
echo "------------------------------------"
echo "Code deployment online successfully!"
echo "------------------------------------"


# auto restart supervisord
COMMON_DIR=/home/kratos/local

NGINX_HOME=$COMMON_DIR/nginx
NGINX_COMMON=/home/kratos/local/nginx/sbin

SUPERVISOR_COMMON=/home/kratos/local/python2.7.5/bin
SUPERVISOR_HOME=$COMMON_DIR/supervisor

if [ $AFFILIATE_HOME = "/home/kratos/srv/AFFILIATE_HADES/" ]; then
   #restart supervisor process
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf start affiliate_hades
      
   #reload nginx conf
   cd $NGINX_HOME/conf/conf.d/
   rm -rf affiliate-upstream.conf
   ln -s affiliate-upstream.hades affiliate-upstream.conf
   $NGINX_COMMON/nginx -s reload
   
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf stop affiliate_boseidon
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf stop proxy_product_boseidon
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf start proxy_product_hades
elif [ $AFFILIATE_HOME = "/home/kratos/srv/AFFILIATE_BOSEIDON/" ]; then
   #restart supervisor process
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf start affiliate_boseidon
     
   #reload nginx conf
   cd $NGINX_HOME/conf/conf.d/
   rm -rf affiliate-upstream.conf
   ln -s affiliate-upstream.boseidon affiliate-upstream.conf
   $NGINX_COMMON/nginx -s reload
   
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf stop affiliate_hades
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf stop proxy_product_hades
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf start proxy_product_boseidon
elif [ $AFFILIATE_HOME = "/home/kratos/srv/API_HADES/" ]; then
   #restart supervisor process
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf start tracking_hades
      
   #reload nginx conf
   cd $NGINX_HOME/conf/conf.d/
   rm -rf tracking-upstream.conf
   ln -s tracking-upstream.hades tracking-upstream.conf
   $NGINX_COMMON/nginx -s reload
   
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf stop tracking_boseidon
elif [ $AFFILIATE_HOME = "/home/kratos/srv/API_BOSEIDON/" ]; then
   #restart supervisor process
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf start tracking_boseidon
     
   #reload nginx conf
   cd $NGINX_HOME/conf/conf.d/
   rm -rf tracking-upstream.conf
   ln -s tracking-upstream.boseidon tracking-upstream.conf
   $NGINX_COMMON/nginx -s reload
   
   $SUPERVISOR_COMMON/supervisorctl -c $SUPERVISOR_HOME/conf/supervisord.conf stop tracking_hades
fi

echo -e "\n"
echo "-------------------------"
echo "Nginx reload successfully"
echo "-------------------------"

echo -e "\n"
echo "============= end ============="