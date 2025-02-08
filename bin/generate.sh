cd "$(dirname "$0")"
docker compose -f ./generator/compose.yaml run --rm app python src/__main__.py "$@"