## change data capture using Debezium

#### logbin configurations

add this in the my.conf in mysql 

[mysqld]
log_bin = mysql-bin
binlog_format = ROW
server_id = 1

Then restart your mysql or container

docker-compose restart mysql


#### Set Up Debezium Connector for MySQL

After MySQL is running with binary logging enabled, you can set up the Debezium connector to monitor changes

```
curl -X POST -H "Content-Type: application/json" \
  --data '{
    "name": "mysql-connector",
    "config": {
      "connector.class": "io.debezium.connector.mysql.MySqlConnector",
      "database.hostname": "mysql",
      "database.port": "3306",
      "database.user": "root",
      "database.password": "rootpassword",
      "database.server.id": "184054",
      "database.server.name": "banking",
      "database.whitelist": "banking",
      "database.history.kafka.bootstrap.servers": "kafka:9092",
      "database.history.kafka.topic": "dbhistory.banking",
      "database.allowPublicKeyRetrieval": "true",                               
      "database.useSSL": "false"                             
    }
  }' http://localhost:8083/connectors


```

Try updating mysql 

curl -X POST "http://127.0.0.1:8002/account/12345/deposit/" -H "Content-Type: application/json" -d '{"amount": 500}'

curl -X POST "http://127.0.0.1:8002/account/12345/deposit/" -H "Content-Type: application/json" -d '{"amount": 500}'


kafka-console-consumer --bootstrap-server localhost:9092 --topic <your-topic-name> --from-beginning
