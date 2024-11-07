SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
docker build -t local-postgres "${SCRIPT_DIR}"
docker network create test_net
docker run --name postgres --network test_net -p 5433:5432 -d local-postgres
