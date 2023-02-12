 FROM tomcat:8-jdk8-corretto
COPY server.xml $CATALINA_HOME/conf/server.xml
COPY context.xml $CATALINA_HOME/conf/context.xml
COPY target/****** /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
CMD ["catalina.sh", "run"]
