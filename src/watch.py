import hupper

from src.index import main


def watch() -> None:
    reloader = hupper.start_reloader("src.index.main")
    reloader.watch_files(["src.index.main"])
    main()


if __name__ == "__main__":
    watch()
