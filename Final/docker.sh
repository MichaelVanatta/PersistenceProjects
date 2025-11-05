cd ./Neo4j
docker run -d --name Neo4jWiki -e NEO4J_AUTH=neo4j/12345678 -p 7474:7474 -p 7687:7687 -v $PWD\data:/data -v $PWD\import:/import -v $PWD\plugins:/plugins neo4j:latest
