import argparse
import httpx

DOCKER_HUB_BASE_URL = "https://hub.docker.com/v2/repositories"


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "org",
        type=str,
        help="Organization that the repository is a part of",
    )
    parser.add_argument(
        "repo",
        type=str,
        help="The repository to get verisons of",
    )

    args = parser.parse_args()

    org, repo = str(args.org), str(args.repo)

    response: httpx.Response = httpx.get(
        f"{DOCKER_HUB_BASE_URL}/{org}/{repo}/tags/?page_size=100"
    )

    response.raise_for_status()

    data: dict = response.json()

    versions = sorted([image["name"] for image in data["results"]])

    for version in versions:
        print(version)


if __name__ == "__main__":
    main()
