#!/bin/bash
# SerpAPI shared utility for BEAR and ECHO
# Usage:
#   serpapi.sh trends "keyword" US "today 12-m"
#   serpapi.sh trends "keyword1,keyword2" US "today 5-y"
#   serpapi.sh search "keyword" US "Chicago, Illinois"
#   serpapi.sh related "keyword" US "today 12-m"
#
# Engines:
#   trends  = Google Trends interest over time
#   related = Google Trends related queries
#   search  = Google Search (for ECHO ad pulls)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VAULT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Load API key
if [ -f "$VAULT_ROOT/.env" ]; then
    export $(grep -v '^#' "$VAULT_ROOT/.env" | xargs)
fi

if [ -z "${SERPAPI_KEY:-}" ]; then
    echo "ERROR: SERPAPI_KEY not found. Add it to $VAULT_ROOT/.env" >&2
    exit 1
fi

ENGINE="${1:?Usage: serpapi.sh <trends|related|search> <keyword> <geo> [date|location]}"
KEYWORD="${2:?Keyword required}"
GEO="${3:-US}"
DATE_OR_LOC="${4:-today 12-m}"

BASE_URL="https://serpapi.com/search.json"

case "$ENGINE" in
    trends)
        curl -s -G "$BASE_URL" \
            --data-urlencode "engine=google_trends" \
            --data-urlencode "q=$KEYWORD" \
            --data-urlencode "geo=$GEO" \
            --data-urlencode "date=$DATE_OR_LOC" \
            --data-urlencode "data_type=TIMESERIES" \
            --data-urlencode "api_key=$SERPAPI_KEY"
        ;;
    related)
        curl -s -G "$BASE_URL" \
            --data-urlencode "engine=google_trends" \
            --data-urlencode "q=$KEYWORD" \
            --data-urlencode "geo=$GEO" \
            --data-urlencode "date=$DATE_OR_LOC" \
            --data-urlencode "data_type=RELATED_QUERIES" \
            --data-urlencode "api_key=$SERPAPI_KEY"
        ;;
    search)
        curl -s -G "$BASE_URL" \
            --data-urlencode "engine=google" \
            --data-urlencode "q=$KEYWORD" \
            --data-urlencode "gl=$GEO" \
            --data-urlencode "location=$DATE_OR_LOC" \
            --data-urlencode "api_key=$SERPAPI_KEY"
        ;;
    *)
        echo "Unknown engine: $ENGINE. Use trends, related, or search." >&2
        exit 1
        ;;
esac
