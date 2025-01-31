cd "$(dirname "$0")"
docker compose -f ./generator/compose.yaml run --rm app python main.py "$@"