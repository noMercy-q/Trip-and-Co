SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
docker build -t local-postgres "${SCRIPT_DIR}"
docker run --name postgres -d local-postgres